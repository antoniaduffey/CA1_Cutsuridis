# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:11:46 2021

@author: parsh
"""

""" Generate weight matrix through storage of random binary patterns
 with the clipped Hebbian learning rule.
 Weights stored in incoming column order for each target cell.
 BPG 19-8-08 """
### imports
import numpy as np
 
### save files
FWGT = 'weights.csv'   # weights file
FPATT = 'pattern.csv' # patterns file
    
###generate weight matrix
num_cell = 100   # number of neurons
num_patt = 5     # number of patterns
num_actpatt = 20 # number of active cells per pattern 
#PC = 0.5;    # percent connectivity (not normally used)

# np.random.rand('state', 0)
np.random.seed()
# np.randrange(0,1)

w = np.zeros((num_cell,num_cell), dtype = int)
p = np.zeros((num_cell, num_patt), dtype = int)


for x in range(0, num_patt):
    # generate pattern
    pr = np.random.permutation(num_cell)
    pi = pr[1:num_actpatt] 
    p[pi,x] = 1
    # store in weight matrix
    z = np.transpose(p[:,x].reshape(100, 1 ))
    y= p[:,x]
    test = np.matmul(p[:,x].reshape(100, 1 ), z)
    w += test

w = w > 0

np.savetxt(FWGT, w, fmt = '%d')
np.savetxt(FPATT, p, fmt = '%d')



    