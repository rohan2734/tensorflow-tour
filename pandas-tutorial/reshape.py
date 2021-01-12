#stack : 

#it is used to stack the prescribed data from columns to indexes, and it return s areshaped data, and series , with mulitlevel index, and having one more new innermost levels compared to old data frame
import pandas as pd
import numpy as np

my_tuple = list(zip(*[[1,2,3,4,5,17,18,19] , [ 11,12,6,7,8,9,10,25]]))
print(my_tuple)

my_tuple2 = list(zip([1,2,3] , [4,5,6]))
print(my_tuple2)

index= pd.MultiIndex.from_tuples(my_tuple,names = ['First','Second'])

df1 = pd.DataFrame(np.random.randn(8,2), index= index,columns = ['A','B'])
print(df1)

df2 = df1[:4] #takes rows from 0 to 3
print(df2)

# print(df1.iloc[0:3,2:5])

