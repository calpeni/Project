#!/usr/bin/env python

"""Script to run the neutral-metabolic model using high performance computing. On the cluster, it will be run multiple times concurrently, with different parameter values."""

__author__ = 'Calum Pennington (c.pennington@imperial.ac.uk)'
__version__ = '0.0.1'

import os
from NormalisationConstants import * # file names
from RunSim import *


i = int(os.getenv('PBS_ARRAY_INDEX'))

R = 1.5
A = 1
c = sc.sqrt(R**2 + 1)
x = sc.sqrt(A / (sc.pi * c))
b_density = calculate_b_density(biggest_body_mass = 1000, highest_resolution = (30, 30), c = c, x = x)

B_0_dispersal = calculate_B_0_dispersal(M = 1000, T = 30 + 273.15, row_index = 30, T_r = 30, T_theta = 30, x = x, distance = 1/3)
# Normalise so the mean dispersal distance of the biggest body mass in the bottom row (hottest, widest) is 1/3 of the row's circumference.

wall_time = 60 * 46
rand_seed = i
interval_rich = 20 # *
sim_name = i
nrows, ncols = 30, 30
max_revolutions = 5

# Body mass
if (i >= 1) & (i <= 20):
	M = 1000
	sample_size = 90
elif (i > 20) & (i <= 40):
	M = 100
	sample_size = 510
elif (i > 40) & (i <= 60):
	M = 10
	sample_size = 2850
else:
	M = 1000
	sample_size = 90

if (i >= 1) & (i <= 60) & (i % 2 == 0):
	max_diversity = True
else:
	max_diversity = False
# Run half with an initial state of max diversity (each individual is a unique species), and half, min diversity (one species).
# (simulated community's species richness at time 0)

# Ratio of the cone's height and base radius (h/x)
if (i > 60) & (i <= 80):
	R = 0
elif (i > 80) & (i <= 100):
	R = 1
elif (i > 100) & (i <= 120):
	R = 2
elif (i > 120) & (i <= 140):
	R = 10
else:
	R = 1.5

# Temperature of each altitudinal band
if (i > 140) & (i <= 160):
	T = sc.around(sc.linspace(0, 15, 30) + 273.15, 2) # 30 rows
else:
	T = sc.around(sc.linspace(10, 25, 30) + 273.15, 2) # *

# Normalisation constant for the dependence of dispersal distance on body mass and temperature
B_0_dispersal = calculate_B_0_dispersal(M = 1000, T = 30 + 273.15, row_index = nrows, T_r = nrows, T_theta = ncols, x = x, distance = 1/3)

if (i > 160) & (i <= 180):
	B_0_dispersal = B_0_dispersal / 10
elif (i > 180) & (i <= 200):
	B_0_dispersal = B_0_dispersal * 10
elif (i > 200) & (i <= 220):
	B_0_dispersal = B_0_dispersal / 2
elif (i > 240) & (i <= 260): # 220 - 240
	B_0_dispersal = B_0_dispersal * 2

# Speciation rate
if (i > 280) & (i <= 300): # 240 - 260
	v = 0.1
elif (i > 320) & (i <= 340): # 260 - 280
	v = 0.0001
else:
	v = 0.01

# Thermal niche width (scale parameter of a normal distribution)
if (i > 340) & (i <= 360): # 280 - 300
	variance_survival = 0.1
elif (i > 360) & (i <= 380): # 300 - 320
	variance_survival = 10
else:
	variance_survival = 1


main(wall_time, rand_seed, sample_size, interval_rich, sim_name,
	R, A, nrows, ncols, M, T,
	b_density, B_0_dispersal, max_revolutions, v, variance_survival,
	max_diversity)

