#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-02-23
Purpose: Translate DNA/RNA to proteins
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        required='TRUE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    codons = args.codons
    seq = args.sequence
    out_fh = args.outfile
    lookup = {}
    for line in codons:
        lookup[line[:3]] = line.rstrip()

    for line in range(0, len(seq), 3):
        triplet = seq[line:line+3].upper()
        if triplet in lookup:
            out_fh.write(lookup[triplet][4])
        else:
            out_fh.write('-')
    print(f'Output written to "{out_fh.name}".')
    out_fh.close()

# --------------------------------------------------


if __name__ == '__main__':
    main()
