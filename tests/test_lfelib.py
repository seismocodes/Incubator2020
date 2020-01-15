import lfelib

def test_version_string():
    assert isinstance(lfelib.__version__, str)


# A few test cases
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

def test_subduction():
    # Subduction zone family
    filename = '080421.14.048'
    stations = ['B039', 'KHBB', 'KRMB', 'KSXB', 'WDC', 'YBH']
    lfelib.find_LFEs.find_LFEs(filename, stations, tbegin, tend, TDUR, filt, freq0, nattempts, \
        waittime, draw, type_threshold, threshold)

def test_strikeslip():
    # Strike-slip fault family
    filename = '080326.08.015'
    stations = ['GCK', 'GFC', 'GHL', 'GSN', 'GWR', 'HOPS', 'KCPB']
    lfelib.find_LFEs.find_LFEs(filename, stations, tbegin, tend, TDUR, filt, freq0, nattempts, \
        waittime, draw, type_threshold, threshold)
