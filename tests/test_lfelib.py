import lfelib

def test_version_string():
    assert isinstance(lfelib.__version__, str)

# A few test cases
   
# Download instrument response
def test_response():
    station_file = 'stations_permanent.txt'
    lfelib.response.get_all_responses(station_file)

# Look at LFEs for March 7th 2020
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
