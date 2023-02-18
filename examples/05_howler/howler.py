#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-02-13
Purpose: Howler exercise
"""

import argparse
import os
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler exercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    
    args =  parser.parse_args()



    if os.path.isfile(args.text):
        args.text = open(args.text)
        
    else:
        args.text = io.StringIO(args.text + '\n')


    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())

    out_fh.close()
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
