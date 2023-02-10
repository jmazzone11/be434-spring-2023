#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-02-09
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    jumper = {'1' : '9', '2' : '8', '3' : '7', '4' : '6', '5' : '0', '6' : '4', '7' : '3', '8' : '2', '9' : '1', '0' : '5'}

    #new_text = '' 
    #for char in text:
   #     new_text += jumper.get(char, char)
        

    #print(new_text)

    new_text = [jumper.get(char, char) for char in text]

    print(''.join(new_text))

# --------------------------------------------------
if __name__ == '__main__':
    main()
