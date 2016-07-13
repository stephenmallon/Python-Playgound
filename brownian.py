# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:53:29 2016

@author: SMALLON
"""

"""
brownian() implements a one dimensional Brownian action (The Wiener Process)

"""

# File = brownian.py

from math import sqrt
from scipy.stats import norm
import numpy as np

def brownian(x0, n, dt, delta, out=None):
    """
    Generate an instance of Brownian motion :
    X(t) = X(0) + N(0, delta**2 * t; 0, t)
    
    """
    x0=np.asarray(x0)
    r=norm.rvs(size=x0.shape + (n,),scale=delta*sqrt(dt))
    
    if out is None:
        out = np.empty(r.shape)
    np.cumsum(r, axis=-1, out=out)
    out += np.expand_dims(x0, axis=-1)

    return out