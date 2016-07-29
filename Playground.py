# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:44:14 2016

@author: SMALLON
"""

def makelist(start, stop, inc):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + inc
    return result
    
mylist = makelist(0,100,0.2)
print (mylist)

#Random Walk Example
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
    
  #HEARTS, SPADES, CLUBS, DIAMONDS
suits = ['H', 'S', 'C', 'D']
card_val = (range(1,11) + [10] *3) * 4
base_names = ['A'] + range(2,11) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)

deck = Series(cal_val, index=cards)

##
book = 7.0

if book > 5.0:
    print('Large Cap')
else:
    print('Small')
