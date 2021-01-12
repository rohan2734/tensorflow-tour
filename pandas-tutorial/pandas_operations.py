# we can apply descriptive static operations
import pandas as pd
import numpy as np

d = pd.date_range('20200301' ,periods=10 )

df=pd.DataFrame( np.random.randn(10,4), index=d,columns=['A','B','C','D'])
print(df)

print(df.mean())#col wise mean

print(df.mean(1))#index wise

s = pd.Series([1,2,3,np.nan,4,5,6,7,8,9], index = d).shift(2) #shifts every value 2 places
print(s)

# s1 = pd.Series([1,2,3,np.nan,4,5,6,7,8,9], index = d)
# print(s1)

# df.sub(s,axis='index')

#functions
print(df)
print(df.apply(np.cumsum))#cumsum ,2nd row first column value is, its value + first column first row, here cumsum is over column

print(df)
print(df.apply(lambda x:x.max() - x.min(),axis=1)) #col wise if no axis is mentioned, or axis =0, when axis =1 , it is row wise

#histogram col wise
print(s.value_counts()) 

#make a series,
s1= pd.Series(['edureka','python','vscode',np.nan,'football','world'])
print(s1.str.upper())

#merging 
#we merge two dataframes, we have 2 functions
#concat and join

# concat : , it concats pandas objects in particular axis, with optional set logic in other axis
# it can also add a layer of heriarchal  indexing on the concatenating index , if the labels are the same, or overlapping on the past axis number

df2 = pd.DataFrame(np.random.randn(10,4))
print(df2)

df3 = [df2[:3], df2[3:7], df2[7:]] #break into pieces
print(df3)

print(pd.concat(df3)) 

#join : 
#left join

leftDf = pd.DataFrame({'A' : [1,2], 'B' : [3,4] })
print(leftDf)

rightDf = pd.DataFrame({'A' : [3,2], 'D' : [4,5] })
print(rightDf)

print(pd.merge(leftDf,rightDf,on='A'))

print(df2.groupby(2).first())
print(df2.groupby(2).sum())
# print(df2.sum(1))


