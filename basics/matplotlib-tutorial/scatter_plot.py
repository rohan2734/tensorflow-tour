# we use this, when we want to plot two or more variables, and we want to find correlation between them
# like how much two variables, are similar to each other
# we are trying to find relationship between the variables

#if variables are far, they are dissimilar, and if they are near , they are similar

import matplotlib.pyplot as plt

x= [1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitscat',color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot')

plt.legend()
plt.show()
