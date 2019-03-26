# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:23:18 2017

@author: AShmelev
"""
# Commercial Flights delay: part1
## Reading and compiling databases
import os
os.system('cls' if os.name == 'nt' else 'clear')

import pandas as pd
import numpy as np

#setting the current working directory (Use only on Alexey Shmelev Desktop):
os.chdir("D:/UW_DATA_SCIENCE/Homeworks2/Final_Project/")

# Merging data frames stored in separate files for each month and create one data frame:
for i in range(12):
    filename = 'flights_' + str(i+1).zfill(2) + '.2015.csv'
    if (i==0):
        flights_data=pd.read_csv('raw_data/' + filename)
        for col in flights_data.columns:
            if 'Unnamed' in col:
                del flights_data[col]
    else:
        flights_temp=pd.read_csv('raw_data/' + filename)
        for col in flights_temp.columns:
            if 'Unnamed' in col:
                del flights_temp[col]
        flights_data=pd.concat([flights_data, flights_temp])

flights_data = flights_data.dropna()
flights_data.to_csv('py_flights_data.2015.csv')
