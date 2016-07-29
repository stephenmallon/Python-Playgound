# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:37:35 2016

@author: SMALLON
"""

def describe(df, col):
    ## Compute the summary stats
    desc = df[col].describe()
    
    ## Change the name of the 50% index to median
    idx = desc.index.tolist()
    idx[5] = 'median'
    desc.index = idx
    return desc