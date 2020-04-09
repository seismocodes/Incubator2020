#!/bin/bash
set -x #echo on

# data command syntax works on macosx, not Ubuntu :(
#year1=$(date -v -3d '+%Y')
#month1=$(date -v -3d '+%m')
#day1=$(date -v -3d '+%d')
#year2=$(date -v -2d '+%Y')
#month2=$(date -v -2d '+%m')
#day2=$(date -v -2d '+%d')

# Works on Ubuntu Linux:
year1=$(date -u -d '3 days ago' '+%Y')
month1=$(date -u -d '3 days ago' '+%m')
day1=$(date -u -d '3 days ago' '+%d')
year2=$(date -u -d '2 days ago' '+%Y')
month2=$(date -u -d '2 days ago' '+%m')
day2=$(date -u -d '2 days ago' '+%d')


getresp -s stations_permanent.txt
lfeall -ff families_permanent.txt -s stations_permanent.txt -t templates -t0 $year1 $month1 $day1 0 0 0 -tf $year2 $month2 $day2 0 0 0 -td 10.0 -d 60.0 -f 1.5 9.0 -f0 1.0 -dt 0.05 -n 10 -w 10.0 -tr MAD -tv 8.0

# Outputs named by date1 (3 days ago):
#./LFEs/080326.08.015/catalog_20200406_000000.csv
#./LFEs/080421.14.048/catalog_20200406_000000.csv
