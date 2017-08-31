#!/usr/bin/env python

""""""

__author__ = 'Calum Pennington (c.pennington@imperial.ac.uk)'
__version__ = '0.0.1'

import pdb, time, pickle
import scipy as sc
from SetUp import * # file names
from NeutralStep import *


def main(wall_time, rand_seed, sample_size, interval_rich, sim_name,
	R, A, nrows, ncols, M, T,#min_temp, max_temp,
	b_density, B_0_dispersal, max_revolutions, v, variance_survival,
	max_diversity=False, species_richness=1,
	B_0_birth_death=1, alpha_birth_death=-0.25, E_birth_death=0.65,
	alpha_dispersal=0.25, E_dispersal=0.65):
	""""""
	#~ pdb.set_trace()
	
	start_time = time.time() # current time in seconds
	finish_time = start_time + (wall_time * 60) # `time.time()` is in s, but `wall_time` is in minutes.
	# Set timer.
	
	if len(T) != nrows:
		sys.exit("Must give a temperature for every altitudinal band (row in the simulated landscape) (i.e. `len(T)` must equal `nrows`).")
	T = T.reshape(-1, 1)
	
	sc.random.seed(rand_seed)
	# Set the seed for random number generation.
	
	c = sc.sqrt(R**2 + 1)
	x = sc.sqrt(A / (sc.pi * c))
	community = initialise_community(nrows, ncols, b_density, M, c, x, species_richness, max_diversity)
	# Set up the simulated community, including the number of individuals and initial species richness.
	
	birth_death_rate_per_temp = metabolic_scaling(M, T, B_0_birth_death, alpha_birth_death, E_birth_death)
	birth_death_map = sc.tile(birth_death_rate_per_temp, (1, ncols))
	birth_map = birth_death_map / birth_death_map.sum() # Re-normalise so probabilities sum to 1.
	death_map = birth_map.ravel()
	# Set up map of birth/death rates. A position's birth rate and death rate are equal.
	# Make a 1D array containing the rate at each altitudinal band (row).
	# Copy the array along axis 1, to make a 2D array containing the rate at each [row, column] position.
	# (Temperature changes with altitude. Birth/death rate changes too, as it depends on temperature. So the rate is the same at positions along a band, but may differ across bands.)
	
	T_opt_map = sc.zeros(community.shape)
	for i in range(nrows):
		T_opt_map[i] = T[i]
	# Set up map of optimum temperatures.
	# At the start of the simulation, an individual's T_opt is the temperature of its position.
	# *Note: zeros in `community` don't represent individuals.
	
	#~ pdb.set_trace()
	dispersal_map_birth, dispersal_map = make_dispersal_map((nrows, ncols), M, T, B_0_dispersal, alpha_dispersal, E_dispersal, max_revolutions, x, c, birth_death_map)
	# Set up dispersal map (net probability of birth and dispersal).
	
	n_generations = 1
	# Initialise a generation count. Start it at 1, as the function increments it after generation 1.
	
	overall_nspp = []
	nspp_per_band = []
	nspp_in_sample = []
	octaves_list = []
	# objects to store results
	# *Cannot preallocate containers as:
		# the function records results throughout
		# while the simulation runs for a set time, the number of steps run of the model depends on computer performance.
	
	overall_nspp.append(sc.unique(community[community > 0]).size)
	tmp = sc.zeros(nrows); tmp2 = sc.zeros(nrows)
	for i in range(nrows):
		tmp[i] = sc.unique(community[i][community[i] > 0]).size
		if i == 0: next # Skip the top altitudinal band.
		else:
			sample = sc.random.choice(community[i][community[i] > 0], sample_size, replace=False)
			tmp2[i] = sc.unique(sample).size
	nspp_per_band.append(tmp); nspp_in_sample.append(tmp2)
	# Record the system's initial state - number of species:
		# overall
		# in each altitudinal band
		# per band, in a random sample of individuals.
	# The simulated community is an array - each item represents an individual and is an integer. The integer's value represents the individual's species identity. To get the number of species, count the number of unique integers.
	# To select values from arrays, you can index arrays with arrays of booleans. `community > 0` returns a boolean array, the same shape as `community`.
	# Sample size is the same per altitudinal band. So, the biggest sample you can take is the amount of individuals in the top band - band with fewest individuals. This is very small, given the amount of individuals in other bands. By omitting the top band, you can take a bigger sample.
	# *Note: stores in columns the spp richness of rows.
	
	#~ pdb.set_trace()
	community_size = community[community > 0].size
	# The community's size (number of individuals) is not `community.size`, as zeros do not represent individuals.
	
	while time.time() <= finish_time: # Run the simulation for the time given by `wall_time`.
		
		for i in range(int(sc.ceil(community_size / 2))): # `range` takes an int argument.
			community, T_opt_map = neutral_step(community, death_map, v, T_opt_map, T, dispersal_map_birth, variance_survival)
		#~ pdb.set_trace()
		# Run the model for one generation.
		# One generation involves a birth or death for every individual. A step of the model involves a birth and death, so there are n/2 steps per generation (n is # individuals). If n is odd, round n/2 up to the next whole number, hence `sc.ceil`.
		
		if n_generations % interval_rich == 0:
			overall_nspp.append(sc.unique(community[community > 0]).size)
			tmp = sc.zeros(nrows); tmp2 = sc.zeros(nrows)
			for i in range(nrows):
				tmp[i] = sc.unique(community[i][community[i] > 0]).size
				if i == 0: next # Skip the top band.
				else:
					sample = sc.random.choice(community[i][community[i] > 0], sample_size, replace=False)
					tmp2[i] = sc.unique(sample).size
			nspp_per_band.append(tmp); nspp_in_sample.append(tmp2)
		#~ pdb.set_trace()
		# Record the number of species, every `interval_rich` generations.
		
		n_generations += 1
		# Update generation count.
	
	overall_nspp = sc.array(overall_nspp, copy=False)
	nspp_per_band = sc.array(nspp_per_band, copy=False)
	nspp_in_sample = sc.array(nspp_in_sample, copy=False)
	# Convert lists to arrays.
	
	with open('%s.pickle' % sim_name, 'wb') as f:
		pickle.dump((overall_nspp, nspp_per_band, nspp_in_sample, octaves_list,
		community, T_opt_map,
		n_generations,
		death_map, dispersal_map_birth, dispersal_map,
		wall_time, rand_seed, sample_size, interval_rich, sim_name,
		R, A, nrows, ncols, M, T,#min_temp, max_temp,
		b_density, B_0_dispersal, max_revolutions, v, variance_survival,
		max_diversity, species_richness,
		B_0_birth_death, alpha_birth_death, E_birth_death,
		alpha_dispersal, E_dispersal), f)
	# Save Python objects to a file using the `pickle` module, which converts objects to byte streams.
	
	return

# `sc.linspace(start, stop, num)` returns `num` evenly spaced numbers, over the interval [`start`, `stop`].
# `sc.tile(A, reps)` constructs an array by repeating `A`. `reps` - number of repetitions along each axis
# `sc.unique` returns an array's unique elements.

## Test
#~ R, A = 1, 1
#~ c = sc.sqrt(R**2 + 1)
#~ x = sc.sqrt(A / (sc.pi * c))
#~ # to get b_density, B_0_dispersal

#~ sim_name = 'RunSim_Aug13'
#~ main(wall_time = 0.5, rand_seed = 1, sample_size = 90, interval_rich = 5, sim_name = sim_name,
	#~ R = R, A = A, nrows = 30, ncols = 30, M = 1000,
	#~ T = sc.around(sc.linspace(10, 25, 30) + 273.15, 2),
	#~ #min_temp = 10, max_temp = 25,
	#~ b_density = b_density, B_0_dispersal = B_0_dispersal, max_revolutions = 5, v = 0.02, variance_survival = 1)

#~ with open('%s.pickle' % sim_name, 'rb') as f:
	#~ overall_nspp, nspp_per_band, nspp_in_sample, octaves_list,\
	#~ community, T_opt_map,\
	#~ n_generations,\
	#~ death_map, dispersal_map_birth, dispersal_map,\
	#~ wall_time, rand_seed, sample_size, interval_rich, sim_name,\
	#~ R, A, nrows, ncols, M, T,\
	#~ b_density, B_0_dispersal, max_revolutions, v, variance_survival,\
	#~ max_diversity, species_richness,\
	#~ B_0_birth_death, alpha_birth_death, E_birth_death,\
	#~ alpha_dispersal, E_dispersal = pickle.load(f)
# min_temp, max_temp
