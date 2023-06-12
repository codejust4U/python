"""
Plotting Histogram in Python using Matplotlib

A histogram is basically used to represent data provided in a form of some groups.It is accurate method for the graphical representation of numerical data distribution.It is a type of bar plot where X-axis represents the bin ranges while Y-axis gives information about frequency.

Creating a Histogram
To create a histogram the first step is to create bin of the ranges, then distribute the whole range of the values into a series of intervals, and count the values which fall into each of the intervals.Bins are clearly identified as consecutive, non-overlapping intervals of variables.The matplotlib.pyplot.hist() function is used to compute and create histogram of x. 
"""


import matplotlib.pyplot as plt
import numpy as np

data1 = np.array([22, 87, 5, 43, 56,
              73, 55, 54, 11,
              20, 51, 5, 79, 31,
              27])

fig1, axis1 = plt.subplots(figsize=(10,8))
axis1.hist(data1, bins=[0,25,50,75,100])

plt.show()


"""
Customization of Histogram
Matplotlib provides a range of different methods to customize histogram. 
matplotlib.pyplot.hist() function itself provides many attributes with the help of which we can modify a histogram.The hist() function provide a patches object which gives access to the properties of the created objects, using this we can modify the plot according to our will.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cl
import matplotlib.ticker as tc

np.random.seed(23685752)
points2 = 10000
bins2 = 20

x2 = np.random.randn(points2)
y2 = .8 ** x2 + np.random.randn(10000) + 25
fig2,axis2 = plt.subplots(1,1,figsize=(10,8),tight_layout=True)

axis2.hist(x2,bins = bins2)
plt.show()

"""
The code below modifies the above histogram for a better view and accurate readings. 
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Creating dataset
np.random.seed(23685752)
N_points = 10000
n_bins = 20

# Creating distribution
x = np.random.randn(N_points)
y = 0.8 ** x + np.random.randn(10000) + 25
legend = ['distribution']

# Creating histogram
fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)

# Remove x, y ticks
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')

# Add padding between axes and labels
axs.xaxis.set_tick_params(pad=5)
axs.yaxis.set_tick_params(pad=10)

# Add x, y gridlines
axs.grid(True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

# Creating histogram
N, bins, patches = axs.hist(x, bins=n_bins)

# Setting color
fracs = ((N ** (1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# Adding extra features
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.title('Customized histogram')

# Show plot
plt.show()

print("------------------------------------------------")

"""
Create a cumulative histogram in Matplotlib

The histogram is a graphical representation of data. We can represent any kind of numeric data in histogram format. In this article, We are going to see how to create a cumulative histogram in Matplotlib

Cumulative frequency: Cumulative frequency analysis is the analysis of the frequency of occurrence of values. It is the total of a frequency and all frequencies so far in a frequency distribution. 

Example:
X contains [1,2,3,4,5] then the cumulative frequency for x is [1,3,6,10,15].

Explanation:
[1,1+2,1+2+3,1+2+3+4,1+2+3+4+5]
"""

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
data3 = [10,20,30,40,50,60]
res3 = stats.cumfreq(data3, numbins=4, defaultreallimits=(1.5,5))
rng3 = np.random.RandomState(seed=12345)
sample3 = stats.norm.rvs(size=1000,random_state=rng3)
res3=stats.cumfreq(sample3,numbins=25)
data3 = res3.lowerlimit+np.linspace(0,res3.binsize*res3.cumcount.size,res3.cumcount.size)
fig3 = plt.figure(figsize=(10,5))
axis3_1 = fig3.add_subplot(1,2,1)
axis3_2 = fig3.add_subplot(1,2,2)
axis3_1.hist(sample3,bins=25,color='gold')
axis3_1.set_title("Histogram")
axis3_2.bar(data3,res3.cumcount,width=4,color='blue',alpha=0.5)
axis3_2.set_title("Cumulative histogram")
axis3_2.set_xlim([data3.min(),data3.max()])
plt.show()


print("------------------------------------------------")

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
data3 = [10,20,30,40,50,60]
res3 = stats.cumfreq(data3, numbins=4, defaultreallimits=(1.5,5))
rng3 = np.random.RandomState(seed=12345)
sample3 = stats.norm.rvs(size=1000,random_state=rng3)
res3=stats.cumfreq(sample3,numbins=25)
data3 = res3.lowerlimit+np.linspace(0,res3.binsize*res3.cumcount.size,res3.cumcount.size)
fig3 = plt.figure(figsize=(10,5))
axis3_1 = fig3.add_subplot(1,2,1)
axis3_2 = fig3.add_subplot(1,2,2)
axis3_1.hist(sample3,bins=25,color='gold')
axis3_1.set_title("Histogram")
axis3_2.bar(data3,data3,width=4,color='blue',alpha=0.6)
axis3_2.set_title("Cumulative histogram")
axis3_2.set_xlim([data3.min(),data3.max()])
plt.show()

print("------------------------------------------------")