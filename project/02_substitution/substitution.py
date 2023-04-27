#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-27
Purpose: substitution cipher
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='substitution cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='SEED',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default='std.out')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    file = args.file

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_letters = random.sample(letters, k=26)
    letter_dict = dict(zip(letters, random_letters))

    for line in file:
        for char in line:
            if char.upper() in letter_dict:
                if args.decode:
                    text = [k for k, letter in letter_dict.items()
                            if letter == char.upper()][0]
                else:
                    text = letter_dict.get(char.upper())
            else:
                text = char
            print(text, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
