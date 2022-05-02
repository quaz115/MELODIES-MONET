"""
test_monet_pair.py
"""
import sys
import argparse
import logging
import yaml

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import xarray as xr

import monet

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
Open dataset
"""
ds = xr.load_dataset(control['model']['test_model']['files'])
logging.info(ds)
