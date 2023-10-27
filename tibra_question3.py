#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:10:05 2023

@author: mwshay
"""

def calcMissing(readings):
    # Write your code here
    from datetime import datetime
    data = []
    missing_data = []
    for idx, reading in enumerate(readings):
        time = datetime.strptime(reading.split('\t')[0], '%m/%d/%Y %H:%M:%S')
        if "Missing" not in reading.split('\t')[1]:
            data.append([time, reading.split('\t')[1]])
        else:
            missing_data.append([time, reading.split('\t')[1]])
    
    ##Use KNN method to fill missing data
    
    #Define the distance between datapoint
    def time_difference(time1, time2):
        time_delta = abs(time1 - time2)
        return time_delta
    
    #Fill the missing data
    k = 3
    fill_data=[]
    for m_idx, m_datapoint in enumerate(missing_data):
        neighbour = []
        for idx, datapoint in enumerate(data):        
            dist = time_difference(datapoint[0], m_datapoint[0])  
            neighbour.append([dist, float(datapoint[1])])
        neighbour.sort()
        knn = neighbour[:k]
        fill_data.append(round(sum(value[1] for value in knn) / k, 3))
        
    print(fill_data)
    return fill_data