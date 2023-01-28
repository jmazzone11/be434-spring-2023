#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-01-28
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g',
                        '--greeting',
                        metavar='str',
                        help='The greeting',
                        default='Howdy',
                        type=str)
    parser.add_argument('-n',
                        '--name',
                        metavar='str',
                        help='Whom to greet',
                        default='Stranger',
                        type=str)
    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    exclamation = '!' if args.excited else '.'

    print(f"{greeting}, {name}{exclamation}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
