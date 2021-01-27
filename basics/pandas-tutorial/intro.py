import pandas as pd
from pandas.core.arrays.sparse import dtype
import numpy as np

#make a series
#np.nan is null value
s = pd.Series([1,2,3,4,5,6,np.nan,8,9,10])

print(s)

#create a dataframe
d = pd.date_range('20200301',periods=10)
print(d)

df1 = pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
print(df1)

#pass ditctionaries
df2 = pd.DataFrame({'A':[1,2,3,4],
                    'B':pd.Timestamp('20200301'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([5]*4,dtype='int32'),
                    'E':pd.Categorical(['True','False','True','False']),
                    'F':'Edureka'
})

print(df2)

print(df2.dtypes)

#6rows, 4 columns
df3= pd.DataFrame(np.random.randn(6,4),index=range(0,6),columns=['A1','A2','A3','A4'])
print(df3)

# s2=pd.Series(1,index=list(range(4)),dtype='float32')
# print(s2)

# a1=np.array([5]*4,dtype='int32')
# print(a1)

df4=pd.DataFrame({
    'A':np.array([1,2,3]),
    'B':pd.Series(np.random.randn(3),index=list(range(3)),dtype='int32')
})
print(df4)