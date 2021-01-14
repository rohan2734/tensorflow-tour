import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(500),index= pd.date_range('1/2/2020',periods=500))
print(ts)

ts = ts.cumsum()
print(ts)

ts.plot()
# plt.show()

ts.to_csv("ts.csv")
ts_read = pd.read_csv(r"D:\Documents\github-projects\tensorflow-ml-ai-freeCodeCamp\pandas-tutorial\ts.csv")
print(ts_read)
