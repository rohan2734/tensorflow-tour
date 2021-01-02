import numpy as np

import time

import sys

# S = range(1000) #take random integer values from 0 to 999

# print(S)
# print(sys.getsizeof(5)*len(S))

# D = np.arange(1000) #arange is similart to range

# print(D)
# print(D.size*D.itemsize)

#numpy occupies less space

SIZE = 10000000

L1 = range(SIZE)
L2= range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)] #sum of elements in list
print((time.time() - start)*1000) #to milliseconds


start = time.time()
result = A1+A2  #sum of elements in array
print((time.time() - start)*1000)

