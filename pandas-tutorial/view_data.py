#how to view data
#it is important to understand the various aspects to view data in order to work
import numpy as np
import pandas as pd


d = pd.date_range('20200301',periods=10)
# print(d)
df1 = pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
print(df1)

#give values of first five rows
print(df1.head())

#gives values of first five columns
print(df1.tail())


#prints index values
print(df1.index)
#prints columns
print(df1.columns)

#to numpy,:gives numpy representaiton of data
print(df1.to_numpy())

#df1.describe gives, count,max,mean, std
print(df1.describe())

#sort each values in row, sorts values in indexes
print(df1.sort_values(by='20200303',axis=1,ascending=False))

print(df1.sort_values(by='A',axis=0,ascending=False))
#default axis is 0
#sort by column C, default ascending
print(df1.sort_values(by='C'))

#sort index#rows
#it sorts the rows indexes
print(df1.sort_index(axis=1,ascending=False))

#it sorts the columns indexes
print(df1.sort_index(axis=0,ascending=False))



