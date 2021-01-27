#plot sin and cos functions
import numpy as np
import matplotlib.pyplot as plt

#define x position
x = np.arange(0,3*np.pi,0.1)

#define y position
# y = np.sin(x)
y = np.cos(x)

plt.plot(x,y)

# plt.show()

arr = np.array([1,2,3])
print(np.exp(arr))
print(np.log(arr)) #log base e , natural log

print(np.log10(arr)) 
