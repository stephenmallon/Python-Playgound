# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 17:01:18 2016

@author: SMALLON
"""
#Get price to book from Y!
#import time
import urllib
#from urllib import urlopen

sp500short =['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']


def yahooKeyStats(stock):
    try:
        sourceCode=urllib.urlopen('http://finance.yahoo.com/q/ks?s='+stock).read()
        pbr = sourceCode.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print("Price to Book Ratio:",pbr)
    except Exception:
        print("Failed In the Main Loop")
    