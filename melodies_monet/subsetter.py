import os
import sys
import argparse
import logging
import yaml
from glob import glob

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

logging.debug(control)

for model in control['model']:
    logging.info('processing:' + model)

    variables = list()
    for dataset in control['model'][model]['mapping']:
        for var in control['model'][model]['mapping'][dataset]:
            variables.append(var)
    logging.info(variables)

    files = sorted(glob(control['model'][model]['files']))
    for file_in in files:
        logging.info(file_in)
        file_out = 'subset_' + file_in

