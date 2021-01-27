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
g = np.array([(1,2,3),(3,4,5)])
print(np.sqrt(g))

#standard deviation
print(np.std(g)) # how each element varies from mean

#addition
#happens element wise, (matrix addition)
h = np.array([(1,2,3),(4,5,6)])
print(g+h) #here in case of lists, if we do that, it concatenates, but in numpy, it calculates the sum

#subtraction

print(g-h)

#multiplication
print(g*h)

#division
print(g/h)

#concatenation
#two ways - vertical stacking, horizontal stacking

print(np.vstack((g,h))) #first g, then h

print(np.hstack((g,h))) #first g , then h

#array to single colum
print(g.ravel())



