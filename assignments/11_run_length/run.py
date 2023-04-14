#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-12
Purpose: Run-length encoding/data compression
"""

import argparse
import os
# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.input):
        with open(args.input, encoding="utf-8") as file:
            args.input = file.read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    bases = args.input

    def frequency(bases):
        current = 0
        while current < len(bases):
            count = 1
            while current < len(
                    bases) - 1 and bases[current] == bases[current+1]:
                count += 1
                current += 1
            if count > 1:
                print(f"{bases[current]}{count}", end="")
            else:
                print(bases[current], end="")
            current += 1

    frequency(bases)


# --------------------------------------------------
if __name__ == '__main__':
    main()
