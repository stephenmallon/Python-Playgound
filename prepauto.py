# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:11:10 2016

@author: SMALLON
"""
def read_auto(pathName = "c:\dat203.1x\mod4", fileName = "Automobile price data _Raw_.csv"):
    ## Load the data  
    import pandas as pd
    import numpy as np
    import os

    ## Read the .csv file
    pathName = pathName
    fileName = fileName
    filePath = os.path.join(pathName, fileName)
    auto_price = pd.read_csv(filePath)

    ## Convert some columns to numeric values
    cols = ['price', 'bore', 'stroke', 
          'horsepower', 'peak-rpm']
    auto_price[cols] = auto_price[cols].convert_objects(convert_numeric = True)
    
    ## Remove rows with missing values
    auto_price.dropna(axis = 0, inplace = True)

    ## Compute the log of the auto price
    auto_price['lnprice'] = np.log(auto_price.price)

    ## Create a column with new levels for the number of cylinders
    auto_price['num-cylinders'] = ['four-or-less' if x in ['two', 'three', 'four'] else 
                                 ('five-six' if x in ['five', 'six'] else 
                                 'eight-twelve') for x in auto_price['num-of-cylinders']]
    return auto_price
