#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 13:09:50 2023

@author: mwshay
"""

import math
import os 
import random
import re
import sys

node_values=[1,3,-1,3,1,5]

   
def maximum_path(node_values):
    # Write your code here
    
    #Define the pyramid 
    pyramid = []
    level = []
    level_num = 1
    
    for node in node_values:
        level.append(node)
        
        if len(level) == level_num:
            pyramid.append(level)
            level = []
            level_num += 1
    
    if level:
        pyramid.append(level)
    
    ##Maximum Path of pyramid
    #Calulate the maximum from the bottom level of pyramid
    for level in range(len(pyramid)-2, -1, -1):
        for level_node in range(len(pyramid[level])):
            pyramid[level][level_node] += max(pyramid[level+1][level_node], pyramid[level+1][level_node+1])
    return pyramid[0][0]  


