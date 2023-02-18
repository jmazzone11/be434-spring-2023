#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-02-13
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file

    for doc in file:
        text = doc.read().rstrip()
        num = 0
        for line in text.split("\n"):
            num += 1
            if args.number:
                print(f"     {num}\t{line}")
            else:
                print(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
