#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-04-28
Purpose: vigenere cipher
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--keyword',
                        help='A keyword',
                        metavar='KEYWORD',
                        type=str,
                        default='CIPHER')

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default='std.out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    keyword = args.keyword.upper()

    def find_letters(file, keyword):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = []
        for line in file:
            letters_count = 0
            letters_index = []
            key_index = []
            for char in line:
                char = char.upper()
                if char in letters:
                    letters_count += 1
                    letters_index.append(letters.index(char))
                    repeat = (keyword * (letters_count //
                              len(keyword) + 1))[:letters_count]
                    key_c = [char for char in repeat if char in letters]
                    key_index.append(letters.index(key_c[-1]))
            if args.decode:
                final = [sum(pair) for pair in zip(
                    letters_index, [-i for i in key_index])]
            else:
                final = [sum(pair) for pair in zip(letters_index, key_index)]
            line_output = []
            for index in final:
                out = letters[index] if index < 26 else letters[(index - 26)]
                line_output.append(out)
            output.append(''.join(line_output))
        return output

    result = ''.join(find_letters(file, keyword))

    file.seek(0)

    counter = 0
    for line in file:
        for char in line:
            if char.upper() in letters:
                correct = result[counter]
                counter += 1
            else:
                correct = char
            print(correct, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
