#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:06:06 2023

@author: mwshay
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 01:45:45 2023

@author: mwshay
"""

import math

def valuation(reqArea, area, price):
    # Write your code here
    
    #Create a dictionary/hashtable to store the price of same size
    hash_table = {}
    for idx, size in enumerate(area):
        if size not in hash_table:
            hash_table[size] = []
        hash_table[size].append(price[idx])
    
    def mean(lst):
        if not lst:
            return 0
        #function of average of input list
        return sum(lst) / len(lst)
    
    def std(lst):
        if not lst or len(lst) == 1:
            return 0
        #function of standard deviation of input list
        mean_val = mean(lst)
        variance = sum((num - mean_val) **2 for num in lst) / (len(lst) -1 )
        standard_deviation = math.sqrt(variance)
        
        return standard_deviation
    
    def check_outliers(key, values):
        '''
        Parameters:
        key:(integer) the key denotes the key in hash table, in this case, the key is the area
        values:(list) the values denotes the values under the key in hash table, in this case, the values denotes the price(s) in of the area
        Return:
        area_price: (float) the calculated price of the area under conditions
        '''
        if len(values) == 0:
            area_price = key * 1000
        elif len(values) == 1:
            area_price = float(values[0])
        else:            
            #check outliers
            outliers = []
            for value in values:
                complist = values.copy()
                complist.pop(values.index(value))
                pm = mean(complist)
                sigma = std(complist)
                if abs(value-pm) > 3 * sigma:
                    outliers.append(value)
            #remove the outlier
            area_price = float(mean([value for value in values if value not in outliers]))
            
        return area_price
    
    #removed outliers hash table
    area = []
    price = []
    for key, values in hash_table.items():
        if check_outliers(key, values) != 0:
            area.append(key)
            price.append([check_outliers(key, values)])

    ##Evaluation of the property price    
    if reqArea in area:
        return int(mean(price[area.index(reqArea)]))
    
    elif reqArea > max(area):
        #find the closest maximum and second max
        area1 = max(area)
        price1 = price[area.index(area1)]
        area2 = max([i for i in area if i != area1])
        price2 = price[area.index(area2)]
        
    elif reqArea < min(area):
        #find the closest minimum and second min
        area1 = min(area)
        price1 = price[area.index(area1)]
        area2 = min([i for i in area if i != area1])
        price2 = price[area.index(area2)]
            
    else:
        #find the closest greater and closest smaller
        area1 = float('inf') #cloest_greater
        area2 = float('-inf') #cloest_smaller
        
        for idx, num in enumerate(area):
            if num > reqArea and num < area1:
                area1 = num
                price1 = price[idx]
            elif num < reqArea and num > area2:
                area2 = num
                price2 = price[idx]
    
    reqPrice = float(price1[0]) + (reqArea - area1)*(float(price2[0])-float(price1[0])) / (area2 - area1)
    
    final_price = max(1000, min(1000000, round(reqPrice)))
    
    return final_price