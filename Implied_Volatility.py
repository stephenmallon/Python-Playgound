# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:36:03 2016

@author: SMALLON
"""

#Import data
import pandas as pd
h5 = pd.HDFStore('./source/vstoxx_data_31032014.h5', 'r')
futures_data = h5['futures_data'] #VSTOXX futures data
options_data = h5['options_data']
h5.close()

futures_data

options_data.info()

options_data[['DATE', 'MATURITY', 'TTM', 'STRIKE', 'PRICE']].head()

options_data['IMP_VOL']

from bsm_functions import *

tol = 0.5 #tolerance level for moneyness
for option in options_data.index:
    #Iterating over all option quotes
    forward = futures_data[futures_data['MATURITY'] == options_data.loc[option]['MATURITY']]['PRICE'].values[0]
    #Picking the right futures values
    if (forward * (1- tol) < options_data.loc[option]['STRIKE'] < forward * (1+tol)):
    #Select for options with moneyness within tolerance
        imp_vol = bsm_call_imp_vol(
        V0, #VSTOXX value
        options_data.loc[option]['STRIKE'],
        options_data.loc[option]['TTM'],
        r,
        options_data.loc[option]['PRICE'],
        sigma_est=2.,   #Estimate for implied volatility
        it=100)
options_data['IMP_VOL'].loc[option] = imp_vol

futures_data['MATURITY']
    #Select column with name MATURITY
options_data.loc[46170]
#Select Data row for index 46170
options_data.loc[46710]['STRIKE']
#Select only value in column STRIKE
plot_data = options_data[options_data['IMP_VOL'] > 0]
maturities = sorted(set(options_data['MATURITY']))

maturities

#Reiterate over all maturities and plot
import matplotlib as plt
#%matplotlib inline
plt.figure(figsize=(8,6))
for maturity in maturities:
    data = plot_data[options_data.MATURITY == maturity]
    #Select data for this maturity
    plt.plot(data['STRIKE'], data['IMP_VOL'], label=maturity.date(), lw=1.5)
    plt.plot(datadata['STRIKE'], data['IMP_VOL'], 'r.')
plt.grid(True)
plt.xlabel('strike')
plt.ylabel('implied volatility of volatility')
plt.legend()
plt.show()
