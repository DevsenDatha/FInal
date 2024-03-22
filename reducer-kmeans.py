#!/usr/bin/python3
import sys
import numpy as np

# Both points and centers are numpy arrays. 
current_center = None
new_center = np.zeros((1,5))
count = 0
centers = []
for line in sys.stdin:
    line = line.strip()
    splits = line.split(',')
    # get the center
    center = splits[0]
    # get your point
    point = np.array(list(map(float,splits[1:]))).reshape(1,5)
    ''' TODO: Write code to compute the new centers based on the number of points per center'''
    ''' Some skeleton code is provided ''' 
    if current_center == center:
        ''' TODO: write code here if the current_center is same as center of new line'''
    else:
        ''' TODO: compute the new centers'''

''' TODO: Account for the last key'''


