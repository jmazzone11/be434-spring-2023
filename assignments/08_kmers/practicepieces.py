#!/usr/bin/env python3
"""
Author : jmazzone <jmazzone@localhost>
Date   : 2023-03-23
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))
                        
    
    parser.add_argument('FILE2',
                        help='Input file 2',
                        type=argparse.FileType('rt'))
                        
    
    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args

# --------------------------------------------------
def find_kmers(file, k):
    """ Find k-mers in string """
    
    output_list = []
    for word in range(len(file) - k + 1):
        output_list.append(file[word:word+k])
    return output_list

    #n = len(seq) - k + 1
    #return [] if n < 1 else [seq[i:i + k] for i in range(n)]
    
def common_elements(list1, list2, k):
    list1 = find_kmers(list1, k)
    list2 = find_kmers(list2, k)
    common = list(set([element for element in list1 if element in list2]))
    values = [f"{element:10} {list1.count(element):5} {list2.count(element):5}" for element in common]
    return '\n'.join(values)

#def common_values(file, list):
 #   return [file.count(line) for line in list]

#def common_elements(file, list):
#    common = [element for element in file if element in list]
#    values = [f"{element} {list1.count(element)} {list2.count(element)}" for element in common]
#    return '\n'.join(values)
    


#def common_elements(list1, list2):
#        return [element for element in list1 if element in list2]

#def common_values(file, list1):
#        return [file.count(line) for line in list1]
    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    k = args.kmer
    file1 = ''.join(args.FILE1.read()).split()
    file2 = ''.join(args.FILE2.read()).split()
    
    results = common_elements(file1, file2, k)
    print(results)
    
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
