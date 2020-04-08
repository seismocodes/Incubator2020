"""
This module contains functions to get instrument responses
from the IRIS DMC or the NCEDC website
"""
import obspy
import obspy.clients.fdsn.client as fdsn
import os
import pandas as pd
import urllib.request

import argparse

def get_from_IRIS(station, network):
    """
    Get instrument response from the IRIS DMC

    Input:
        type station = string
        station = Name of seismic station
        type network = string
        network = Name of seismic network
    Ouput:
        None
    """
    fdsn_client = fdsn.Client('IRIS')
    inventory = fdsn_client.get_stations(network=network, \
        station=station, level='response')
    inventory.write(os.path.join('data', 'response/' + network + '_' + station + '.xml'), \
        format='STATIONXML')

def get_from_NCEDC(station, network):
    """
    Get instrument response from the NCEDC website

    Input:
        type station = string
        station = Name of seismic station
        type network = string
        network = Name of seismic network
    Ouput:
        None
    """
    url = 'http://service.ncedc.org/fdsnws/station/1/query?net=' + \
        network + '&sta=' + station + \
        '&level=response&format=xml&includeavailability=true'
    s = urllib.request.urlopen(url)
    contents = s.read()
    file = open(os.path.join('data', 'response/' + network + '_' + station + '.xml'), 'wb')
    file.write(contents)
    file.close()

def get_all_responses(station_file):
    """
    Get instrument response for all the stations

    Input:
        type station_file = string
        station_file = Name of input file with the list of seismic stations
    Output:
        None
    """
    # Get the network and names the stations
    staloc = pd.read_csv(os.path.join(station_file), \
        sep=r'\s{1,}', header=None, engine='python')
    staloc.columns = ['station', 'network', 'channels', 'location', \
        'server', 'latitude', 'longitude', 'time_on', 'time_off']

    # Create directory for xml files
    namedir = os.path.join('data', 'response')
    if not os.path.exists(namedir):
        os.makedirs(namedir)

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

def cli():
    """Command line parser."""
    parser = argparse.ArgumentParser( \
        description='Get instrument response for all the stations')
    parser.add_argument('-s', type=str, dest='station_file', \
        required=True, \
        help='Input file with names of the seismic stations')
    args = parser.parse_args()
    print(args)
    get_all_responses(args.station_file)

if __name__ == '__main__':
    cli()
