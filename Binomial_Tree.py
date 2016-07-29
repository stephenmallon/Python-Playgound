# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 19:51:47 2016

@author: SMALLON
"""

import numpy as np
import scipy.stats as ss
import time 

def BinomialTree(type,S0, K, r, sigma, T, N=2000):
    #calculate delta T    
    deltaT = float(T) / N
 
    # up and down factor will be constant for the tree so we calculate outside the loop
    u = np.exp(sigma * np.sqrt(deltaT))
    d = 1.0 / u
 
   
    # Initialise our f_{i,j} tree with zeros
    fs = [[0.0 for j in xrange(i + 1)] for i in xrange(N + 1)]
    
    #store the tree in a triangular matrix
    #this is the closest to theory
    
    #no need for the stock tree
 
    #rates are fixed so the probability of up and down are fixed.
    #this is used to make sure the drift is the risk free rate
    a = np.exp(r * deltaT)
    p = (a - d) / (u - d)
    oneMinusP = 1.0 - p

# Compute the leaves, f_{N, j}
for j in xrange(i+1):
    if type =="C":
        fs[N][j] = max(S0 * u**j * d**(N - j) - K, 0.0)
    else:
        fs[N][j] = max(-S0 * u**j * d**(N - j) + K, 0.0)
            
 #calculate backward the option prices
for i in xrange(N-1, -1, -1):
    for j in xrange(i + 1):
        fs[i][j] = np.exp(-r * deltaT) * (p * fs[i + 1][j + 1] + oneMinusP * fs[i + 1][j])
                  
        
return fs[0][0]
    
    
S0 = 100.0
K = 100.0
r=0.1
sigma = 0.30
T = 3
Otype='C'

print ("S0\tstock price at time 0:", S0)
print ("K\tstrike price:", K)
print ("r\tcontinuously compounded risk-free rate:", r)
print ("sigma\tvolatility of the stock price per year:", sigma)
print ("T\ttime to maturity in trading years:", T)

t=time.time()
c_BT = BinomialTree(Otype,S0, K, r, sigma, T,1500)
elapsed=time.time()-t
print ("c_BT\tBinomial Tree:", c_BT, elapsed)