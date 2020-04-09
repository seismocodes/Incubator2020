# Incubator2020
![Package Build Status](https://github.com/ArianeDucellier/Incubator2020/workflows/Package/badge.svg)
![Daily Run](https://github.com/ArianeDucellier/Incubator2020/workflows/CronJob/badge.svg)

This repository contains all files related to the codes developed during Winter 2020 Incubator project Daily monitoring of low-frequency earthquake activity and slow slip event occurrence.

## To run the code:

Install and activate environment with latest released version of lfelib
```
conda env create -f environment.yml
conda activate lfelib
pip install --extra-index-url https://test.pypi.org/simple/ lfelib
```

Run `lfefind` command to look for LFEs for two families during the day of April 21st 2008. It will create two output files catalog.csv in the directory LFEs/family_name. Each of the pickle files contains a pandas dataframe with columns year, month, day, hour, minute, second where the LFE was detected, corresponding value of the cross-correlation, number of channels that were used to detect the LFE.
```
lfefind -t 080326.08.015 -s GCK GFC -t0 2008 4 21 0 0 0 -tf 2008 4 22 0 0 0
```

## Development environment

To make changes to the codebase and create new package releases install a development environment:

```
conda env create -f environment-dev.yml
conda activate lfelib-dev
poetry install
```

Run tests
```
poetry run pytest
```
