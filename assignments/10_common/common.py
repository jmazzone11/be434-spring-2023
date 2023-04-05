#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-04
Purpose: Find common words
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    def word_select(text):
        words = set()
        for line in text:
            for word in line.split():
                words.add(word)
        return words

    file1 = word_select(args.file1)
    file2 = word_select(args.file2)
    common = '\n'.join(set.intersection(file1, file2))
    if args.outfile:
        args.outfile.write(common)
    else:
        print(common)


# --------------------------------------------------
if __name__ == '__main__':
    main()
