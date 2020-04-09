import lfelib
import pandas as pd
import os

# data directory is relative to wherever script is run
DATADIR = os.path.join(os.getcwd(), 'examples')

def test_version_string():
    assert isinstance(lfelib.__version__, str)


def test_getresp():
    # Get station response files
    station_file = os.path.join(DATADIR, 'stations_permanent.txt')
    lfelib.response.get_all_responses(station_file)

    assert os.path.isfile(os.path.join(DATADIR, 'response/NC_GCK.xml'))
    assert os.path.isfile(os.path.join(DATADIR, 'response/NC_GFC.xml'))
    assert os.path.isfile(os.path.join(DATADIR, 'response/PB_B039.xml'))
    assert os.path.isfile(os.path.join(DATADIR, 'response/NC_KHBB.xml'))


def test_lfefind():
    # Strike-slip fault family
    TDUR = 10.0
    filt = (1.5, 9.0)
    freq0 = 1.0
    nattempts = 10
    waittime = 10.0
    draw = False
    type_threshold = 'MAD'
    threshold = 8

    # Look at LFEs for April 21st 2008
    tbegin = (2008, 4, 21, 0, 0, 0)
    tend = (2008, 4, 22, 0, 0, 0)
    filename = '080326.08.015'
    stations = ['GCK', 'GFC']
    output = 'results.csv'

    lfelib.lfe.find_LFEs(filename, stations, tbegin, tend, output, TDUR, filt, freq0, nattempts, \
                         waittime, draw, type_threshold, threshold)
    # Load results
    df = pd.read_csv(f'LFEs/{filename}/{output}', index_col=0)

    assert os.path.isfile(f'LFEs/{filename}/{output}')
    assert df.shape == (3,8)


def test_find_all_LFEs():
    family_file = 'families_permanent.txt'
    station_file = 'stations_permanent.txt'
    template_dir = 'templates'
    tbegin = (2020, 3, 7, 0, 0, 0)
    tend = (2020, 3, 8, 0, 0, 0)
    TDUR = 10.0
    duration = 60.0
    filt = (1.5, 9.0)
    freq0 = 1.0
    dt = 0.05
    nattempts = 10
    waittime = 10.0
    type_threshold = 'MAD'
    threshold = 8.0
    lfelib.lfe_all.find_LFEs(family_file, station_file, template_dir, tbegin, tend, \
        TDUR, duration, filt, freq0, dt, nattempts, waittime, type_threshold, \
        threshold)
