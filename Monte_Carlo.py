# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:39:38 2016

@author: SMALLON
"""

from bsm_functions import bsm_call_value
S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2
bsm_call_value(S0, K, T, r, sigma)
