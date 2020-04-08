import lfelib
import pandas as pd
import os

# Test command line utilities:
#[tool.poetry.scripts]
#lfefind = 'lfelib.lfe:cli'
#getresp = 'lfelib.response:cli'
#lfeall = 'lfelib.lfe_all:cli'

def test_version_string():
    assert isinstance(lfelib.__version__, str)


def test_getresp():
    # Get station response files
    station_file = 'stations_permanent.txt'
    lfelib.response.get_all_responses(station_file)

    assert os.path.isfile('data/response/NC_GCK.xml')
    assert os.path.isfile('data/response/NC_GFC.xml')
    assert os.path.isfile('data/response/PB_B039.xml')


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


# Add simple test that doesn't take too long to run, ensuring this function works as expected
#def test_lfeall():
#    print('TODO')
