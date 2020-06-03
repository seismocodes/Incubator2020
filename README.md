# lfelib
![Package Build Status](https://github.com/seismocodes/lfelib/workflows/Package/badge.svg)
![Daily Run](https://github.com/seismocodes/lfelib/workflows/CronJob/badge.svg)

This repository contains all files related to the codes developed during [University of Washington eScience Winter 2020 Incubator](https://escience.washington.edu/winter-2020-incubator-projects/) project: "Daily monitoring of low-frequency earthquake activity and slow slip event occurrence."

## To run the code:

Install and activate environment with latest released version of lfelib
```
conda env create -f environment.yml
conda activate lfelib
pip install --extra-index-url https://test.pypi.org/simple/ lfelib
```

Run `lfeall` command to look for LFEs for two families during the day of April 21st 2020. It will create two output files catalog.csv in the directory LFEs/family_name. Each of the pickle files contains a pandas dataframe with columns year, month, day, hour, minute, second where the LFE was detected, corresponding value of the cross-correlation, number of channels that were used to detect the LFE.
```
cd examples
getresp -s stations_permanent.txt
lfeall -ff families_permanent.txt -s stations_permanent.txt -t templates -t0 2020 4 21 0 0 0 -tf 2020 4 22 0 0 0
```

## Install development environment for testing and packaging

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

Release a new version on Test PyPi
```
# First edit "version" in pyproject.toml file
git tag 0.0.3
git push --tags
```
