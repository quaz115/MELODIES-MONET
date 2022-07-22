import sys
sys.path.append('..')
sys.path.insert(0, '/Users/davidfillmore/EarthSystem/monetio')
sys.path.insert(0, '/Users/davidfillmore/EarthSystem/monet')
from melodies_monet import driver

an = driver.analysis()
an.control = 'mm_musica.yaml'
an.read_control()
an.control_dict

an.open_models()
an.models

an.open_obs()
