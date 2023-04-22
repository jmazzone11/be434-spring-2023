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

    parser.add_argument('text', 
                        metavar='text', 
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))
    

    return parser.parse_args()


# --------------------------------------------------
def f(n):
    return n ** n

def main():
    """Make a jazz noise here"""

    args = get_args()
    #text = args.text
    #vowel = args.vowel

    #new_text = [ vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char for char in text]
    #print(new_text)
    #print(f(3))
    
    with open('exercises.csv') as fh:

        values = fh.readline().rstrip().split(',')


# --------------------------------------------------
if __name__ == '__main__':
    main()
