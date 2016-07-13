# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:03:11 2016

@author: SMALLON
"""

#Valuation in Black-Scholes Including Vega function and implied volatility

#Analytical Black-Scholes

def bsm_call_value(S0, K, T, r, sigma):
    """ Valuation of European Call Option in BSM Model.
    Analytical Formula
    
    Parameters
    ==========
    S0: float
        initial stock/index level
    K:  float
        strike price
    T:  float
        maturity date (in year fractions)
    r: float
        constant risk free short rate
    sigma:  float
        volatility factor in difusion form
        
    Returns
    =========
    value: float
        present value of European call option
    """
    from math import log, sqrt, exp
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0/K) + (r + 0.05 * sigma **2) * T) / (sigma * sqrt(T))
    d2 = (log(S0/K) + (r - 0.5 * sigma **2) * T) / (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2,0.0,1.0))
    return value

#Vega Function
def bsm_vega(S0, K, T, r, sigma):
    """ Vega of European option in BSM model.
    
    Parameters
    ==========
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date in year fractions
    r : float
        constant risk-free short rate
    sigma : float
        volatility factor in diffusion term
        
    Returns
    ========
    vega : float
        partial derivative of BSM formula with respect to sigma
    """
from math import log, sqrt
from scipy import stats

S0 = float(S0)
d1 = (log(S0/K) + (r + 0.5 * sigma ** 2) * T / (sigma * sqrt(T)))
vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
return vega

#Implied volatility function

def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    """Implied volatility function of European call option in BSM model
    Parameters
    ==========
    S:0 float
        initial stock/index price
    K: float
        strike price
    T:float
        maturity date in year fractions
    sigma_est:float
        estimate of implied volatility
    it:integer
        number of iterations
    
    Returns
    =======
    sigma_est:float
        numerically estimated implied volatility
    """
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0) / bsm_vega(S0, K, T, r, sigma_est))
    
    return sigma_est
    
# Set initial price
# Input value for V0
    
#Set risk free short rate
#Input value for r
    
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
    (forward = futures_data[futures_data['MATURITY'] == \
        options_data.loc[option]['MATURITY']]['PRICE'].values[0])
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
%matplotlib inline
plt.figure(figsize=(8,6))
for maturity in maturities:
    data = plot_data[options_data.MATURITY == maturity]
    #Select data for this maturity
    plt.plot(data['STRIKE'], data['IMP_VOL'], label=maturity.date(), lw=1.5)
    plt.plot(datadata['STRIKE'], data['IMP_VOL'], 'r.')
plt.grid(True)
plt.xlabel('strike')
plt.ylabel('implied volatility of volatility)
plt.legend()
plt.show()
