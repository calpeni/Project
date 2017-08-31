#!/bin/bash

#PBS -l walltime=48:00:00
#PBS -l select=1:ncpus=1:mem=1gb

module load anaconda/2.4.1
source activate python3
module load intel-suite

echo "Simulation is about to run."
python $WORK/ParamValuesHPC.py
mv *.pickle $WORK
echo "Simulation has ended."
