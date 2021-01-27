# it is used when , we need to show parts of a whole
#ex: percentage of market share 

import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols=['c','m','r','b']

plt.pie(slices,
    labels=activities,
    colors=cols,
    startangle=180,
    shadow=True,
    explode=(0,0.1,0,0),
    autopct=('%1.1f%%')
)

plt.title('pie plot')
plt.show()