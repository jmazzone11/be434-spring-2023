#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-27
Purpose: caesar shift
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        metavar='NUMBER',
                        type=int,
                        help='A number to shift',
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
    file = args.file

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def find_letters(file):
        for line in file:
            for char in line:
                if char.upper() in letters:
                    if letters.index(char.upper()) + args.number < 26:
                        number = letters.index(char.upper()) + args.number
                        code.append(number)
                    else:
                        number = letters.index(char.upper()) + args.number - 26
                    print(letters[number], end='')
                else:
                    print(char, end='')

    def decode_letters(file):
        for line in file:
            for char in line:
                if char.upper() in letters:
                    if letters.index(char.upper()) - args.number >= 0:
                        number = letters.index(char.upper())-args.number
                        code.append(number)
                    else:
                        number = 26 + (letters.index(char.upper())-args.number)
                        code.append(number)
                    print(letters[number], end='')
                else:
                    print(char, end='')

    code = []

    if args.decode:
        decode_letters(file)
    else:
        find_letters(file)


# --------------------------------------------------
if __name__ == '__main__':
    main()
