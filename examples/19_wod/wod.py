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
    random.seed(args.seed)
    exercises = read_csv(args.file)

    if not exercises: 
        sys.exit(f'No usable data in --file "{args.file.name}"')
    
    num_exercises = len(exercises)
    if args.num > num_exercises:
        sys.exit(f'--num "{args.num}" > exercises "{num_exercises}"')

    wod = []
    for exercise, low, high in random.sample(exercises, k =args.num): 
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps/2)
        wod.append((exercise, reps))
    
    print(tabulate(wod, headers= ('Exercise', 'Reps')))

def read_csv(fh):
    """Read the CSV input"""

    
    reader = csv.DictReader(fh, delimiter = ',')
    exercises = []
    for rec in reader:
        name, reps = rec.get('exercise'), rec.get('reps')
        if name and reps: 
            match = re.match('(\d+)-(\d+)', reps)
            #low, high = map(int, reps.split('-'))
            if match:
                low, high = map(int, match.groups())
                exercises.append((name, low, high))
    
    return exercises

# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]

# --------------------------------------------------
if __name__ == '__main__':
    main()
