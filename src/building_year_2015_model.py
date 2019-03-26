# -*- coding=: utf-8 -*-
"""
Created on Fri Mar 24 13:23:18 2017

@author: AShmelev
"""
# Commercial Flights delay: part3
# Building 2015 Arrival delay model

# Clearing console:
import os
os.system('cls' if os.name == 'nt' else 'clear')
#setting the current working directory (Use only on Alexey Shmelev Desktop):
os.chdir("D:/UW_DATA_SCIENCE/Homeworks2/Final_Project/")


# import packages:
import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Reading cleaned and filtered 2051 dataset:
flights_data_2015=pd.read_csv('flights_data.2015.filtered.csv')
del flights_data_2015['Unnamed: 0']


# Columns that carry redundant information:
#to_drop=['DAY_OF_MONTH', 'FL_DATE', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID', 'ORIGIN_CITY_NAME', 'DEST_AIRPORT_ID', 'DEST_CITY_NAME', 'AIR_TIME', 'ORIGIN_LOAD', 'DEST_LOAD']
to_drop=['DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID', 'ORIGIN_CITY_NAME', 'DEST_AIRPORT_ID', 'DEST_CITY_NAME', 'AIR_TIME', 'ORIGIN_LOAD', 'DEST_LOAD']

flights_data_2015=flights_data_2015.drop(to_drop, axis=1)


# Defining categorical variables:
# cat_col=['MONTH', 'DAY_OF_WEEK', 'CARRIER', 'ORIGIN', 'ORIGIN_STATE_ABR', 'DEST', 'DEST_STATE_ABR','DEP_HOUR']
cat_col=['MONTH', 'FL_DATE', 'DAY_OF_WEEK', 'CARRIER', 'ORIGIN', 'ORIGIN_STATE_ABR', 'DEST', 'DEST_STATE_ABR','DEP_HOUR']


# Converting selected  columns into categorical values: 
for col in cat_col: flights_data_2015[col]=flights_data_2015[col].astype('category')

# display categories of leftover columns (as a QC):
flights_data_2015.dtypes

# Before Z-scaling distance, save its SD and MEAN in separate variables
# These will be used for 2016 dataset 
DISTANCE_SD=np.std(flights_data_2015['DISTANCE'])
DISTANCE_MEAN=np.mean(flights_data_2015['DISTANCE'])

# Z-scoring DDISTANCE:
flights_data_2015['DISTANCE']=zscore(flights_data_2015['DISTANCE'])


# Log transforming delay:
#flights_data_2015['ARR_DELAY']=np.log(90+flights_data_2015['ARR_DELAY'])

# Creating linear model:
import statsmodels.api as sm

y=flights_data_2015['ARR_DELAY']
X=flights_data_2015.drop(['ORIGIN_STATE_ABR', 'DEST_STATE_ABR', 'ARR_DELAY'], axis=1)
M = pd.get_dummies(X).as_matrix()
from sklearn.linear_model import Ridge
ridgereg = Ridge(alpha=0.3, normalize=True)
ridgereg.fit(M, y) 
y_pred = ridgereg.predict(M)
plt.plot(y-y_pred,'.')
np.std(y-y_pred)
plt.hist(y, np.linspace(0, 7,1000), facecolor='green', alpha=0.75, label='DELAY');
plt.hist(y_pred, np.linspace(0, 7,100), facecolor='green', alpha=0.75, label='Pred DELAY');
plt.show()

plt.hist(y, np.linspace(-50,300, 1000), facecolor='green', alpha=0.75, label='DELAY');
plt.hist(np.log(np.log(y+90)), np.linspace(1, 3, 1000), facecolor='green', alpha=0.75, label='DELAY');


X.head
