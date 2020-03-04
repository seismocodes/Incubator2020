"""
This module contains functions to get instrument response
from the IRIS DMC or the NCEDC website
"""

import obspy
import obspy.clients.fdsn.client as fdsn
import urllib.request

def get_from_IRIS(station, network):
    """
    """
    fdsn_client = fdsn.Client('IRIS')
    inventory = fdsn_client.get_stations(network=network, \
        station=station, level='response')
    inventory.write('data/response/' + network + '_' + station + '.xml', \
        format='STATIONXML')

def get_from_NCEDC(station, network):
    """
    """
    url = 'http://service.ncedc.org/fdsnws/station/1/query?net=' + \
        network + '&sta=' + station + \
        '&level=response&format=xml&includeavailability=true'
    s = urllib.request.urlopen(url)
    contents = s.read()
    file = open('data/response/' + network + '_' + station + '.xml', 'wb')
    file.write(contents)
    file.close()
