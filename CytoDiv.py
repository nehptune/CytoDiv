# CytoDiv calculates cytometric diversity from flow cytometry data
# This method is based on Li (1997), but is extended to include more parameters from the cytogram
# Sophie Clayton, 2013
# sclayton@uw.edu

import numpy as np
import matplotlib.pyplot as plt

# input data - this should be a .csv file


# calculate diversity indices
def divCalc(cyt, Ncat, Nbit):
    # cyt is an array containing the flow cytometry data
    # it can be 2, 3 or 4-D depending on the analysis to be done
 
    # check the shape of the input array
    dim = cyt.shape

    # bin the data Ncat categories
    binned = 
    totbin = 

    # calculate diversity indices
    pi = binned/totbin.
    p = pi[pi>0]
    N0 = sum(p**0) # total number of categories present
    H = - sum(p*log(p)) # Shannon-Wiener index
    N2 = sum(p**2) # Simpson's index
    D = 1 - N2 # Simpson's index of diversity
    J = H/log(N0) # evenness

    return p N0 H N2 D J

# write the data out to a file

