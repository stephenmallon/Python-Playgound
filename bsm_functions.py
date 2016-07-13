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
    d1 = (log(S0/K) + (r + 0.5 * sigma **2) * T) / (sigma * sqrt(T))
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
    
