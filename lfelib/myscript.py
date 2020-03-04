""" Script to launch analysis on all families """

import pandas as pd

from get_responses import get_from_IRIS, get_from_NCEDC
from find_all_LFEs import find_LFEs

station_file = 'data/stations_permanent.txt'

# Get the network and names the stations
staloc = pd.read_csv(station_file, sep=r'\s{1,}', header=None, engine='python')
staloc.columns = ['station', 'network', 'channels', 'location', \
    'server', 'latitude', 'longitude', 'time_on', 'time_off']

# Download the response of the stations
for ir in range(0, len(staloc)):
    station = staloc['station'][ir]
    network = staloc['network'][ir]
    server = staloc['server'][ir]
    # First case: we can get the data from IRIS
    if (server == 'IRIS'):
        get_from_IRIS(station, network)
    # Second case: we get the data from NCEDC
    elif (server == 'NCEDC'):
        get_from_NCEDC(station, network)
    else:
        raise ValueError('You can only download data from IRIS and NCEDC')

# Look for LFEs for all families
family_file = 'data/families_permanent.txt'
station_file = 'data/stations_permanent.txt'
template_dir = 'data/templates'
tbegin = (2020, 2, 24, 0, 0, 0)
tend = (2020, 2, 25, 0, 0, 0)
TDUR = 10.0
duration = 60.0
filt = (1.5, 9.0)
freq0 = 1.0
dt = 0.05
nattempts = 10
waittime = 10.0
type_threshold = 'MAD'
threshold = 8.0
    
find_LFEs(family_file, station_file, template_dir, tbegin, tend, \
    TDUR, duration, filt, freq0, dt, nattempts, waittime, type_threshold, \
    threshold)