#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-02-09
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('solfege',
                        metavar='str',
                        type=str,
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    solfege = args.solfege
    notes = {'Do': 'A deer, a female deer', 'Re': 'A drop of golden sun',
             'Mi': 'A name I call myself', 'Fa': 'A long long way to run',
             'Sol': 'A needle pulling thread', 'La': 'A note to follow sol',
             'Ti': 'A drink with jam and bread'}

    for line in solfege:
        if line in notes:
            text = notes.get(line)
            print(line + ', ' + text)
        else:
            print(f'I don\'t know "{line}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
