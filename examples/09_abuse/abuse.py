#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-03-18
Purpose: Heap abuse
"""

import argparse
import os
import random
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--number',
                        help='The number of insults',
                        metavar='int',
                        type=int,
                        default=3)
    
    parser.add_argument('-a',
                        '--adjectives',
                        help='The number of adjectives per insult',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    adjectives = """
        bankrupt base caterwauling corrupt cullionly detestable dishonest false
        filthsome filthy foolish foul gross heedless indistinguishable infected
        insatiate irksome lascivious lecherous loathsome lubbery old peevish
        rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
        thin-faced toad-spotted unmannered vile wall-eyed
        """.strip().split()

    nouns = """
        Judas Satan ape ass barbermonger beggar block boy braggart butt
        carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
        gull harpy jack jolthead knave liar lunatic maw milksop minion
        ratcatcher recreant rogue scold slave swine traitor varlet villain worm
        """.strip().split()
    #random.seed(args.seed)

    #for n in range(args.number):
    #    print(f"You {', '.join(random.sample(adjectives, args.adjectives))} {random.choice(nouns)}!")
    
   
    x = 'foo', 'bar', 'baz'
    _, val, _ = x

    print(val)


# --------------------------------------------------
if __name__ == '__main__':
    main()
