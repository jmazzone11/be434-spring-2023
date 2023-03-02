#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-02-25
Purpose: practice
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='practice',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='wordcount.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    x = args.file

    print(type(x))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
