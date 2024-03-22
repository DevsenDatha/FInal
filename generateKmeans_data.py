#!/usr/bin/python
import random

''' TODO: Use random function with a seed that corresponds to your DePaulID'''

#Generate 2M 5-dimensional data points with random values between 0 and 1.
k_meansData = [[random.random() for column in range(5)] for row in range(2000000)]

#Output the data file
with open('kmeans_data.csv', 'w') as f:
    for row in k_meansData:
        f.write(','.join(map(str, row)) + '\n')
