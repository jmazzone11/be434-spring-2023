#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-01
Purpose: Filter delimited records
"""

import argparse
import csv
import re
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        required='TRUE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        required='TRUE',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='OUTFILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default="out.csv")

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)
    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    val = args.val

    header = writer.fieldnames

    if args.col and args.col not in header:
        print(f'--col "{args.col}" not a valid column!\n', file=sys.stderr)
        sys.exit(1)

    num = 0
    for line in reader:
        if args.col:
            colinput = line[args.col]
        else:
            colinput = ",".join(line.values())
        if re.search(val, colinput, re.IGNORECASE):
            writer.writerow(line)
            num += 1

    print(f'Done, wrote {num} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
