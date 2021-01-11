# 

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(211)
#2 vertical plots, 1 horizontal, 1 position
# plt.subplot(121)
# 1 vertical, 2 horizontal, 1 position
# plt.subplot(2,2,1)
#2 verrtical,2 horizontal, 1 position

plt.plot(t1,f(t1),'bo',t2,f(t2))


plt.subplot(212)
#2 vertical plots, 1 horizontal, 1 position
# plt.subplot(122)
#1 vertical, 2 horizontal, 2 position
# plt.subplot(2,2,2)
#2 vertical,2 horizontal,2 position
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()



