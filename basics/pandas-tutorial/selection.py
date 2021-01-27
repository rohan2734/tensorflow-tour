import pandas as pd
import numpy as np

d = pd.date_range('20200301' ,periods=10 )

df=pd.DataFrame( np.random.randn(10,4), index=d,columns=['A','B','C','D'])
print(df)

#access a single column values with row indexes
print(df['C'])

#access rows using slicing
print(df[0:3]) #prints from 0 to 2 row

#select by labels
print(df.loc[d[0]]) #this gets the data of the 0th row in each column

#selecting data on multiaxes by labels
print(df.loc[:,['A','C']])

print(df.loc['20200301':'20200305','A':'C'])

#reduce the dimentsions of the data
print(df.loc['20200301','A':'D'])

#scalar value using df.at
print(df.at[d[0],'C'])

#get values from 4th row using indexes
print(df.iloc[3])

print(df.iloc[2:5,1:3])

# print(df[0:1])
# print(df.loc['20200301'])

#boolean indexing
#prints only the values in column A, whose values are greater than 0
print(df[df['A'] > 0])  

#reindexing
df2 =df.reindex(index = d[0:4], columns = list(df.columns) + ['E'])
df2.loc[d[0]:d[1],'E']=1
print(df2)

print(df2.isnull())

# print(df2.dropna())
df2=df2.fillna(value=2)

print(pd.isna(df2))