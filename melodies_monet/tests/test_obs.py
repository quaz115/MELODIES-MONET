"""
pytest test_observation.py
"""
import sys
sys.path.insert(0, '..')
import driver

"""
define a variable in the global scope
to hold a driver.observation object
and be shared across unit tests
"""
analysis = None


def test_init():
    global analysis
    analysis = driver.analysis()
    assert True


def test_read_control():
    global analysis
    analysis.read_control()
    assert True

def test_open_obs():
    global analysis
    analysis.open_obs()
    for obs_set in analysis.obs.keys():
        print(analysis.obs[obs_set])
    assert True

def test_obs_to_df():
    global analysis
    for obs_set in analysis.obs.keys():
        analysis.obs[obs_set].obs_to_df()
    assert True

def test_cleanup():
    global analysis
    del analysis
    assert True
