#qunatitative varibles -histogram
#categorical variables - bar graph


#ex to plot gdp growth of every city, at that time,we chose bargraph, since we need to see cities growth
#ex: how much each age group, contributes to gdp growth

import matplotlib.pyplot as plt

population_ages=[22,55,62,45,21,22,34,42,42
,4,99,102,110,120,121,122,130,111,115,112
,80,75,65,64,43,44,42,48]

bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype="bar",rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('histogram')

plt.legend()

plt.show()