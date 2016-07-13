# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:00:19 2016

@author: SMALLON
"""

#Holding Period Return
"""Calculate Holding Period returns where
EP: end price
SP: start price
APR = nominal annual percentage rate
DIV: dividents earnd
"""
hpr = (EP-SP+DIV)/SP
REFF = ((1+(APR/n))^n-1)