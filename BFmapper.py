#!/usr/bin/env python3

import sys
from pybloom import BloomFilter

#TODO: Load the Bloom filter from a file
bloom_filter_file = 'path/to/your/bloom_filter.bloom'
bloom_filter = BloomFilter.fromfile(open(bloom_filter_file, 'rb'))

def find_membership(depaulid,bloom_filter,number):
'''TODO: Write code to find membership'''

for line in sys.stdin:
    data = line.strip()
    '''TODO: process additional filter clauses in Dwdate'''

    '''TODO: Check for membership in the Bloom filter for the join clause.'''
    

