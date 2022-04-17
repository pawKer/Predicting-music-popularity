#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function    # (at top of module)
import warnings
#warnings.filterwarnings('always')
import json
import time
import csv
import pandas as pd
import numpy as np

from sklearn.preprocessing import scale, MinMaxScaler

def scale_data_standardize(data, columns):
    # Keep data in a temp variable for testing
    scaled_data = data.copy()

    # Normalization
    #scaled_data[columns] = MinMaxScaler().fit_transform(scaled_data[columns])

    #Standardization
    scaled_data[columns] = scale(scaled_data[columns])

    # Return data
    return scaled_data

def scale_data_normalize(data, columns):
    # Keep data in a temp variable for testing
    scaled_data = data.copy()

    # Normalization
    scaled_data[columns] = MinMaxScaler().fit_transform(scaled_data[columns])

    # Return data
    return scaled_data

def label_data(data, threshold_value):
    # Make a copy of the data to which we will ad labels and then remove any 
    # columns that we will not need
    # This is currently a duplicate of the functionality above - could maybe only do this in one place

    labeled_data = data.copy()
    threshold = threshold_value
    labels = []
    labeled_popular = 0
    labeled_notpopular = 0
    for item in data['popularity']:
        if item > threshold:
            labels.append(1)
            labeled_popular = labeled_popular + 1
        else:
            labels.append(0)
            labeled_notpopular = labeled_notpopular + 1
    labeled_data['is_popular'] = labels

    print('Number of popular examples after thresholding : ', labeled_popular)
    print('Number of not popular examples after thresholding : ', labeled_notpopular)
    return labeled_data
def label_data_combined(data, threshold_sp, threshold_yt, threshold_st):
    # Make a copy of the data to which we will ad labels and then remove any 
    # columns that we will not need
    # This is currently a duplicate of the functionality above - could maybe only do this in one place

    labeled_data = data.copy()
    labels = []
    labeled_popular = 0
    labeled_notpopular = 0
    for item in data[['popularity', 'youtube_view_count', 'total_no_streams']].values:
        if item[0] > threshold_sp or item[1] > threshold_yt or item[2] > threshold_st:
            labels.append(1)
            labeled_popular = labeled_popular + 1
        else:
            labels.append(0)
            labeled_notpopular = labeled_notpopular + 1
    labeled_data['is_popular'] = labels

    print('Number of popular examples after thresholding : ', labeled_popular)
    print('Number of not popular examples after thresholding : ', labeled_notpopular)
    return labeled_data
    
def label_data_yt(data, threshold_sp, threshold_yt):
    # Make a copy of the data to which we will ad labels and then remove any 
    # columns that we will not need
    # This is currently a duplicate of the functionality above - could maybe only do this in one place

    labeled_data = data.copy()
    labels = []
    labeled_popular = 0
    labeled_notpopular = 0
    for item in data[['popularity', 'youtube_view_count']].values:
        if item[0] > threshold_sp or item[1] > threshold_yt:
            labels.append(1)
            labeled_popular = labeled_popular + 1
        else:
            labels.append(0)
            labeled_notpopular = labeled_notpopular + 1
    labeled_data['is_popular'] = labels

    print('Number of popular examples after thresholding : ', labeled_popular)
    print('Number of not popular examples after thresholding : ', labeled_notpopular)
    return labeled_data
    


