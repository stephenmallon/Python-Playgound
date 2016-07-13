# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:13:00 2016

@author: SMALLON
"""

#Monte Carlo Valuation of European Stock Option
#Black-Scholes model
#bsm_mcs_euro.py
#
import numpy as np
#parameter values
S0 = 100. #initial index level
K = 105   #strike price
T = 1.0   #time-to-maturity
r = 0.05  #riskless short rate
sigma = 0.2 #volatility

I = 100000 #number of simulations

#valuation algorithm
z= np.random.standard_normal(I) #psuedorandom numbers
ST = S0 * np.exp((r- 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z) #index values at maturiry
hT = np.maximum(ST - K, 0) #inner values at maturity
C0 = np.exp(-r * T) * np.sum(hT) / I #Monte Carlo Estimator
#result output
print ("The Value of European Call option is %5.3f" %C0)