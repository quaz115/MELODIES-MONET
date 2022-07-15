import os
import sys
import argparse
import logging
import yaml

import math
import numpy as np
import scipy as sp
import pandas as pd
import xarray as xr

from field_generators import gaussian_plume_2d

parser = argparse.ArgumentParser()
parser.add_argument('--control', type=str,
    default='control.yaml',
    help='yaml control file')
parser.add_argument('--logfile', type=str,
    default=sys.stdout,
    help='log file (default stdout)')
parser.add_argument('--debug', action='store_true',
    help='set logging level to debug')
args = parser.parse_args()

"""
Setup logging
"""
logging_level = logging.DEBUG if args.debug else logging.INFO
logging.basicConfig(stream=args.logfile, level=logging_level)

"""
Read YAML control
"""
with open(args.control, 'r') as f:
    control = yaml.safe_load(f)

"""
Generate datetime arrays
"""
start_time = pd.to_datetime(control['analysis']['start_time'])
end_time = pd.to_datetime(control['analysis']['end_time'])
datetime_indices = pd.date_range(start_time, end_time,
    freq=control['test_setup']['freq'])
ntime = len(datetime_indices)
datetimes = [np.datetime64(dt) for dt in datetime_indices]

"""
Generate uniform grid
"""
nlat = control['test_setup']['grid']['nlat']
nlon = control['test_setup']['grid']['nlon']
lat_edges = np.linspace(-90, 90, nlat+1, endpoint=True, dtype=float)
lat = 0.5 * (lat_edges[0:nlat] + lat_edges[1:nlat+1])
lat_min, lat_max = lat_edges[0:nlat], lat_edges[1:nlat+1]
deg_to_rad = math.pi / 180.0
weight = np.abs(np.sin(deg_to_rad * lat_max) - np.sin(deg_to_rad * lat_min))
lon_edges = np.linspace(-180, 180, nlon+1, endpoint=True, dtype=float)
lon = 0.5 * (lon_edges[0:nlon] + lon_edges[1:nlon+1])

logging.info((ntime, nlat, nlon))

"""
Generate xarray data arrays
"""
time_da = xr.DataArray(datetimes, attrs={'longname': 'datetime'})
lat_da = xr.DataArray(lat, attrs={'longname': 'latitude', 'units': 'deg North'})
lon_da = xr.DataArray(lon, attrs={'longname': 'longitude', 'units': 'deg East'})

"""
Generate random test fields
"""
np.random.seed(control['test_setup']['random_seed'])
field_names = control['model']['test_model']['variables'].keys()
ds_dict = dict()

for field_name in field_names:
    units = control['model']['test_model']['variables'][field_name]['units']
    field_info = control['model']['test_model']['variables'][field_name]

    if field_info['test_generator'] == 'random_uniform':
        field = np.random.rand(ntime, nlat, nlon)
    if field_info['test_generator'] == 'gaussian_plume_2d':
        field = gaussian_plume_2d(lon_da, lat_da, time_da, field_info['generator_params'])

    field_da = xr.DataArray(
        field, coords=[time_da, lat_da, lon_da],
        dims=['time', 'lat', 'lon'], attrs={'units': units})
    ds_dict[field_name] = field_da

ds = xr.Dataset(ds_dict)
ds.to_netcdf(control['model']['test_model']['files'])
