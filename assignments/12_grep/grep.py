#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-21
Purpose: Python grep
"""

import argparse
import sys
import re

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    pattern = args.pattern

    file = args.file

    for i in file:
        file_name = i.name + ':' if len(file) > 1 else ''
        for line in i:
            if args.insensitive:
                if re.search(pattern, line, re.IGNORECASE):
                    print(f'{file_name}{line}', end='', file=args.outfile)
            else:
                if re.search(pattern, line):
                    print(f'{file_name}{line}', end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
