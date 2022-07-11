"""
pytest test_analysis.py
"""
import sys
sys.path.insert(0, '..')
import driver

"""
define a variable in the global scope
to hold a driver.analysis object
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


def test_open_models():
    global analysis
    analysis.open_models()
    print(analysis.models)
    assert True


def test_open_obs():
    global analysis
    analysis.open_obs()
    print(analysis.obs)
    assert True


def test_cleanup():
    global analysis
    del analysis
    assert True
