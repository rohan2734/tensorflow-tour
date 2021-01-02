import numpy as np

a = np.array([(1,2,3),(2,3,4)])

#to know whether 2 dimension or 1 dimension array

# print(a.ndim)
# print(a.itemsize)
# print(a.dtype)

print(a.size) #total elements in array
print(a.shape) 

#we can also reshape and slicing
#reshape  , means, changing the rows and columns to columns and rows

b = np.array([(1,2,3,4),(3,4,5,6)])
print(b)

# b= b.reshape(4 ,2)
# print(b)

#slicing, 
#extracting elements from array

print(b[0,2]) #3

#to print 4 and 6
print(b[0:,3]) # [0:], means all the rows , that inlcudes 0th row as well

#now to print only 4 and 6
c = np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])
print(c[0:2,3])

d = np.linspace(1,3,5) #print 5 values, between 1 and 3, and are equally spaced
print(d)

#minimum , maximum, sum

e = np.array([1,2,3])
#max
print(e.max())

#min
print(e.min())

#sum
print(e.sum())

f = np.array([(1,2,3),(3,4,5)])
#sum of axis 0 (sum of columns)
print(f.sum(axis=0))

#sum of axis 1(sum of columns)
print(f.sum(axis=1))

#Finding square root 