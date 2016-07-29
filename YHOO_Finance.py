# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:17:46 2016

@author: SMALLON
"""

from yahoo_finance import Share
yahoo = Share('YHOO')
goog = Share('GOOG')
print(yahoo.get_ebitda())
print(yahoo.get_earnings_share())
print(yahoo.get_price_book())
print(goog.get_ebitda())
print(goog.get_earnings_share())
print(goog.get_price_book())

from yahoo_finance import Share
IBB = Share('IBB')
print(IBB.get_ebitda())


from yahoo_finance import Share
li = ['YHOO','GOOG']
yahoo = Share('YHOO')
goog = Share('GOOG')
print(yahoo.get_book_value())
for i in li:
    t = Share(i)
    print(i)
    print(t.get_book_value())
    


from pprint import pprint
from yahoo_finance import Share
yahoo = Share('YHOO')
print(yahoo.get_ebitda())
pprint(yahoo.get_info())

