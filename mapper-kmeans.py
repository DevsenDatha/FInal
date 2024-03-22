#!/usr/bin/python3
import sys
import numpy as np

try:    # if centers have been generated
        ''' You can name the centers.txt file to correspond to the ith iteration. Currently, it is initial.'''
        with open('centers.txt', 'r') as f:
        '''TODO: Write code to read centers.txt file and populate centers array. Each center array is a numpy array of floats.''' 



except: # randomly generate centers
        '''TODO: Write code to populate centers array with random values. Each center array is a numpy array.'''


# print('centers are: ', centers)
for line in sys.stdin:
    ''' TODO: Initialize a point from the line. Point is a numpy array of floats'''
    ''' TODO: Find distance of point with different centers'''
    ''' TODO: Find the minimum distance'''
    ''' TODO: Print the closest center index and the point'''
    ''' If there are 5 centers from index 0..4 and one point is 0.7151199917287518,0.8237243932807248,0.6357409798969764,0.8439461724231083,0.5358627934388042, then output format is
    2, 0.7151199917287518,0.8237243932807248,0.6357409798969764,0.8439461724231083,0.5358627934388042 where the index 2 means it is closest to the third center with index of 2''' 
         

