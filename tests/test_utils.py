import lfelib.utils
import pandas as pd
import os
import pickle
import obspy
import obspy.clients.fdsn.client as fdsn
import urllib

# data directory is relative to wherever script is run
DATADIR = os.path.join(os.getcwd(), 'data')

# Begin and end time of analysis
def convert_dates(tbegin, tend):
    t1 = obspy.UTCDateTime(year=tbegin[0], month=tbegin[1], \
        day=tbegin[2], hour=tbegin[3], minute=tbegin[4], \
        second=tbegin[5])
    t2 = obspy.UTCDateTime(year=tend[0], month=tend[1], \
        day=tend[2], hour=tend[3], minute=tend[4], \
        second=tend[5])
    duration = (nt - 1) * dt
    Tstart = t1 - TDUR
    Tend = t2 + duration + TDUR
    return Tstart,Tend


def test_read_station_metadata():
    # ['station', 'network', 'channels', 'location', 'server', 'latitude', 'longitude']
    staloc = pd.read_csv('station_locations.txt', sep=r'\s{1,}',
                          header=None, engine='python')

    assert len(staloc.columns) == 7


# Simple test case parameters
filename='080326.08.015'
station = 'GCK'
network = 'NC'
location = '--'
channels = 'EHZ'
dt = 0.05
nt = 1201
TDUR = 10.0
filt = (1.5, 9.0)
nattempts = 1.0
waittime = 1.0
tbegin = (2008, 4, 21, 0, 0, 0)
tend = (2008, 4, 22, 0, 0, 0)
errorfile = filename + '.txt'

# Takes a while for many stations
def test_download_response():
    station_file = 'stations_permanent.txt'
    lfelib.response.get_all_responses(station_file)

def test_read_template():
    templatefile = 'templates/' + filename + '/' + station + '.pkl'
    with open(templatefile, 'rb') as f:
        data = pickle.load(f)

    assert type(data) == list
    assert isinstance(data[0], obspy.core.trace.Trace)


def test_instrument_response_from_NCEDC():
    url = 'http://service.ncedc.org/fdsnws/station/1/query?net=' + \
        network + '&sta=' + station + \
        '&level=response&format=xml&includeavailability=true'
    s = urllib.request.urlopen(url)
    contents = s.read()
    file = open(DATADIR + '/response/' + network + '_' + station + '.xml', 'wb')
    file.write(contents)
    file.close()


def test_invalid_station_NCEDC():
    # NOTE: should raise an error for this case
    station='junk'
    Tstart,Tend = convert_dates(tbegin, tend)
    (D, orientation) = lfelib.utils.get_data.get_from_NCEDC(station, network, channels, location,
    Tstart, Tend, filt, dt, nattempts, waittime, errorfile, DATADIR)

    assert (D,orientation) == (0,0)


def test_valid_station_NCEDC():
    station='GCK'
    Tstart,Tend = convert_dates(tbegin, tend)
    (D, orientation) = lfelib.utils.get_data.get_from_NCEDC(station, network, channels, location,
    Tstart, Tend, filt, dt, nattempts, waittime, errorfile, DATADIR)


def test_instrument_response_from_IRIS():
    station = 'B039'
    network = 'PB'
    fdsn_client = fdsn.Client('IRIS')
    inventory = fdsn_client.get_stations(network=network, \
        station=station, level='response')
    inventory.write(DATADIR + '/response/' + network + '_' + station + '.xml', \
        format='STATIONXML')


def test_invalid_station_IRIS():
    station='JUNK'
    Tstart,Tend = convert_dates(tbegin, tend)
    (D, orientation) = lfelib.utils.get_data.get_from_IRIS(station, network, channels, location,
    Tstart, Tend, filt, dt, nattempts, waittime, errorfile, DATADIR)



def test_valid_station_IRIS():
    station='GCK'
    Tstart,Tend = convert_dates(tbegin, tend)
    (D, orientation) = lfelib.utils.get_data.get_from_IRIS(station, network, channels, location,
    Tstart, Tend, filt, dt, nattempts, waittime, errorfile, DATADIR)
