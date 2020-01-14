# Incubator2020
![Action Status](https://github.com/ArianeDucellier/Incubator2020/workflows/CI/badge.svg)

This repository contains all files related to the codes developed during Winter 2020 Incubator project Daily monitoring of low-frequency earthquake activity and slow slip event occurrence.

## To run the code:

Install environment:

conda env create -f environment.yml

Activate environment:

source activate LFEcatalog

Go to source directory:

cd src

Run the code:

python find_LFEs.py

It should look for LFEs for two families during the day of April 21st 2008. It will create two output files catalog.pkl in the directory LFEs/family_name. Each of the pickle files contains a pandas dataframe with columns year, month, day, hour, minute, second where the LFE was detected, corresponding value of the cross-correlation, number of channels that were used to detect the LFE.
