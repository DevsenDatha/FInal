#!/usr/bin/python
import random
import csv

#Get the initial cluster centers using random points selection.'''
def clusterCenters(data, k):
    ''' TODO: Use random function with a seed that corresponds to your DePaulID'''
    ''' TODO: Return a sample of k data points from data'''

with open('kmeans_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    '''TODO: Extract individual data from each cell into data variable.'''

'''TODO: Chosen number of k clusters in kNum.'''

initialCenters = clusterCenters(data, kNum)
with open('centers.txt', 'w') as f:
    ''' TODO: output centers from initialCenters in the same format as in kmeans_data.csv'''
