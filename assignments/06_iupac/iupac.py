#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-03-02
Purpose: Expand IUPAC codes
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        type=str,
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default=[sys.stdout])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq
    out_fh = args.outfile

    base = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 'U': 'U',
            'R': '[AG]', 'Y': '[CT]', 'S': '[GC]', 'W': '[AT]',
            'K': '[GT]', 'M': '[AC]', 'B': '[CGT]', 'D': '[AGT]',
            'H': '[ACT]', 'V': '[ACG]', 'N': '[ACGT]'}
    if out_fh != [sys.stdout]:
        with out_fh as file_out:
            for line in seq:
                print(line + ' ', file=file_out, end='')
                for char in line:
                    print(base.get(char, char), end='', file=file_out)
                print(file=file_out)
            print(f'Done, see output in "{out_fh.name}"')
    else:
        for line in seq:
            print(line + ' ', end='')
            for char in line:
                print(base.get(char, char), end="")
            print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
