# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:15:11 2016

@author: SMALLON
"""

#Count number of bases in string of nucleotides
def count_v10(dna,base):
    m=[]
    return sum(c==base for c in dna)

#Makes a random list

import random

def generate_string(N, alphabet='ACGT'):
    return ''.join([random.choice(alphabet) for i in range(N)])

