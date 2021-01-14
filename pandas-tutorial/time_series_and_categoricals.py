import pandas as pd
import numpy as np

dates = pd.date_range ('3/3/2020',periods=100,freq='S')
print(dates) #frequency of S ,means that, it will generate frequency with seconds

ts = pd.Series(np.random.randint(0,500,len(dates)),index=dates)
# print(np.random.randint(0,500,len(dates)))
print(ts)

print(ts.resample('5min').sum())

#timezone representation
dates2= pd.date_range('3/3/2020',periods=5,freq='S')
ts2= pd.Series(np.random.randn(len(dates2)),dates2)
print(ts2)

ts_utc = ts.tz_localize('UTC')
print(ts_utc)

print(ts_utc.tz_convert('US/Eastern'))

dates3= pd.date_range('3/3/2020',periods=5,freq='M')
ts3 = pd.Series(np.random.randn(len(dates3)) , dates3)
print(ts3) 

ps = ts3.to_period()
print(ps)

print(ps.to_timestamp())

df = pd.DataFrame({'id' : [1,2,3,4,5,6],#id is column, its values are its row values
                   "grade": ['a','b','c','b','a','e']
                    })
print(df)

df['Grade'] = df['grade'].astype('category') #ignores repeated values
# print(df['Grade'])

#rename the categories of df['Grade']
df['Grade'].cat.categories = ["very bad","good","very good","excellent",]
print(df)

df['Grade']= df["Grade"].cat.set_categories(['very good', "bad" , "very bad" ,"good","medium"])
print(df['Grade'])