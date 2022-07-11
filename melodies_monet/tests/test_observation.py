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
control = dict()
observation = None


def test_read_control_yaml(control_yaml):
    import yaml
    global control
    with open(control_yaml, 'r') as f:
        control = yaml.safe_load(f)


def test_init():
    global observation
    observation = driver.observation()
    assert True

