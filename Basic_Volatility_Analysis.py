# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:02:50 2016

@author: SMALLON
"""

#Volatility Analytics from Web - Basic
#Example Google
import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib

#Retieve Data from Google
goog = web.DataReader('GOOG', data_source='google', start='3/14/2009', end= '4/14/2014')
goog.tail()
#Analytics
goog['Log_Ret'] = np.log(goog['Close']/goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)

#Plot Results
%matplotlib inline
goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8,6))
