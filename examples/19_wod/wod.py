#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-03-30
Purpose: Rock the Casbah
"""

import argparse
import csv
import io
import random
from numpy import row_stack
from tabulate import tabulate
from pprint import pprint
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='num',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='Input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    with open('inputs/exercises.csv') as fh:
        values = fh.readline().rstrip().split(',')
    print(type(values))
    
# --------------------------------------------------

# --------------------------------------------------
if __name__ == '__main__':
    main()
