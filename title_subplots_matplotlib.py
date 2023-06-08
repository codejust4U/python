"""
How to Add Title to Subplots in Matplotlib?

In this article, we will see how to add a title to subplots in Matplotlib? Let’s discuss some concepts :

Matplotlib : Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was introduced by John Hunter in the year 2002.
Subplots : The subplots() function in pyplot module of matplotlib library is used to create a figure and a set of subplots. Subplots are required when we want to show two or more plots in same figure.
Title of a plot : The title() method in matplotlib module is used to specify title of the visualization depicted and displays the title using various attributes.
Steps Needed
Import Libraries
Create/ Load data
Make subplot
Plot subplot
Set title to subplots.
"""

"""
Example 1: (Using set_title() method)

We use matplotlib.axes._axes.Axes.set_title(label) method to set title (string label) for the current subplot Axes.
"""

import numpy as np
import matplotlib.pyplot as plt
data1 = np.array([5,2,7,8])

fig1 , axis1 = plt.subplots(2,2)

axis1[0,0].plot(data1,data1,)
axis1[0,1].plot(data1,data1*3)
axis1[1,0].plot(data1*data1)
axis1[1,1].plot(data1*data1*data1)

axis1[0,0].set_title('Linear')
axis1[0,1].set_title('Triple')
axis1[1,0].set_title('square')
axis1[1,1].set_title('Cube')

fig1.tight_layout()
plt.show()

print("-------------------------------------------------------------")

import numpy as np
import matplotlib.pyplot as plt
data1 = np.array([5,2,7,8])

fig1 , axis1 = plt.subplots(2,2)

axis1[0,0].plot(data1,data1,)
axis1[0,1].plot(data1,data1*3)
axis1[1,0].plot(data1*data1)
axis1[1,1].plot(data1*data1*data1)

axis1[0,0].title.set_text('Linear')
axis1[0,1].title.set_text('Triple')
axis1[1,0].title.set_text('square')
axis1[1,1].title.set_text('Cube')

fig1.tight_layout()
plt.show()

print("-------------------------------------------------------------")

"""
Example 3: (Using plt.gca().set_title() method)

If you use Matlab-like style in the interactive plotting, then you could use plt.gca() to get the reference of the current axes of the subplot and combine set_title() method to set title to the subplots in Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

data2 = np.array([5, 2, 7, 8])

fig2, axis2 = plt.subplots(2, 2)

title2 = ["Linear", "Triple", "Square", "Cube"]
values2 = [data2, data2 * 3, data2 * data2, data2 * data2 * data2]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.plot(data2, values2[i])
    plt.gca().set_title(title2[i])

fig2.tight_layout()
plt.show()
print("-------------------------------------------------------------")
"""
How to Set a Single Main Title for All the Subplots in Matplotlib?

A title in Matplotlib library describes the main subject of plotting the graphs. Setting a title for just one plot is easy using the title() method. By using this function only the individual title plots can be set but not a single title for all subplots. Hence, to set a single main title for all subplots, suptitle() method is used.

Syntax: suptitle(self, t, **kwargs)

Parameters: This method accept the following parameters that are discussed below:

t : This parameter is the title text.
x: This parameter is the x location of the text in figure coordinates.
y: This parameter is the y location of the text in figure coordinates.
horizontalalignment, ha : This parameter is the horizontal alignment of the text relative to (x, y).
verticalalignment, va : This parameter is the vertical alignment of the text relative to (x, y).
fontsize, size : This parameter is the font size of the text.
fontweight, weight : This parameter is the font weight of the text.
Returns: This method returns the Text instance of the title.

Setting a Single Title for All the Subplots
Example 1:
In this example, we will import the required library and create a 2*2 plot. We are creating random data by using random.randint to plot our graph and then setting a single title for all the subplots.
"""

import numpy as np
import matplotlib.pyplot as plt

fig3, axis3 = plt.subplots(2,2)

axis3[0][0].plot(np.random.randint(0,5,3),np.random.randint(0,5,3))
axis3[0][1].plot(np.random.randint(0,5,3),np.random.randint(0,5,3))
axis3[1][0].plot(np.random.randint(0,5,3),np.random.randint(0,5,3))
axis3[1][1].plot(np.random.randint(0,5,3),np.random.randint(0,5,3))

plt.suptitle("Setting the single title for all plots",fontsize=30)

plt.show()

print("-------------------------------------------------------------")

"""
Example 2:
Here, we are creating data to plot our graph and using a marker.


"""

import numpy as np
import matplotlib.pyplot as plt

fig4, (axis4, axis5) = plt.subplots(1, 2, figsize=(12, 5))

x1 = [1, 2, 3, 4, 5, 6]
y1 = [45, 34, 30, 45, 50, 38]
y2 = [36, 28, 30, 40, 38, 48]

labels = ["Student1", "Student2"]

fig4.suptitle("Marks in different subjects", fontsize=20)

# Assign the line plot to a variable
graph1, = axis4.plot(x1, y1, 'o-', color='green')  

# Assign the line plot to a variable
graph2, = axis5.plot(x1, y2, 'o-', color='red')   

# Specify handles argument as a list
fig4.legend(handles=[graph1, graph2], labels=labels, loc="upper right")  

# Adjust the left margin
plt.subplots_adjust(left=0.09) 

plt.show()
print("-------------------------------------------------------------")

"""
How to Turn Off the Axes for Subplots in Matplotlib?

In this article, we are going to discuss how to turn off the axes of subplots using matplotlib module. We can turn off the axes for subplots and plots using the below methods:

Method 1: Using matplotlib.axes.Axes.axis()

To turn off the axes for subplots, we will matplotlib.axes.Axes.axis() method here.
"""

import matplotlib.pyplot as plt
import matplotlib.tri as m_tri
import numpy as np


x_data = np.asarray([0, 1, 2, 3, 0.5,
                1.5, 2.5, 1, 2,
                1.5])
 
y_data = np.asarray([0, 0, 0, 0, 1.0,
                1.0, 1.0, 2, 2,
                3.0])
 
triangles_data = [
            [0, 1, 4], [1, 5, 4],
            [2, 6, 5], [4, 5, 7],
            [5, 6, 8], [5, 8, 7],
            [7, 8, 9], [1, 2, 5],
            [2, 3, 6]
            ]

triangles1 = m_tri.Triangulation(x_data,y_data, triangles_data)

z_result = np.cos(1.5*x_data) * np.cos(1.5*y_data)

fig5, axis6 = plt.subplots()

axis6.tricontourf(triangles1,z_result)
axis6.triplot(triangles1,'go-',color='#fff')

axis6.set_axis_off()

axis6.set_title("Illustration of triangle")

plt.show()
print("-------------------------------------------------------------")

import numpy as np
import matplotlib.pyplot as plt

x_data2 = np.array([24.40, 110.25, 20.05,
                22.00, 61.90, 7.80,
                15.00])
 
y_data2 = np.array([24.40, 110.25, 20.05,
                22.00, 61.90, 7.80,
                15.00])

fig6, axis7 = plt.subplots()
axis7.xcorr(x_data2,y_data2, maxlags=6, color='red')

axis7.set_axis_off()

axis7.set_title("Graph of time series")
plt.show()
print("-------------------------------------------------------------")
import matplotlib.pyplot as plt

# assigning x and y coordinates
x_data3 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
x_data4 = [6,8,2,9,3]
y_data3 = []
y_data4 = []
for i in range(len(x_data3)):
    y_data3.append(max(0,x_data3[i]))



axis8 = plt.plot(x_data3,y_data3, color='red')


plt.axis('off')

plt.title("ReLU function graph")

plt.show()


for i in range(len(x_data4)):
    y_data4.append(max(0,x_data4[i]))

axis9 = plt.plot(x_data4,y_data4, color='blue')
plt.axis('off')

plt.title("ReLU function graph")

plt.show()

print("-------------------------------------------------------------")

import matplotlib.pyplot as plt

# assigning x and y coordinates
x_data3 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
x_data4 = [6,8,2,9,3]
y_data3 = []
y_data4 = []
for i in range(len(x_data3)):
    y_data3.append(max(0,x_data3[i]))



axis8 = plt.plot(x_data3,y_data3, color='red')


plt.axis('off')

plt.title("ReLU function graph")

plt.show()


for i in range(len(x_data4)):
    y_data4.append(max(0,x_data4[i]))

axis9 = plt.plot(x_data4,y_data4, color='blue')
plt.axis('off')

plt.title("ReLU function graph")

plt.show()

print("-------------------------------------------------------------")


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

fig7 = plt.figure()

fig7.set_figheight(8)
fig7.set_figwidth(8)

spec1 = gridspec.GridSpec(
    ncols=2, nrows=2, width_ratios=[2, 1], wspace=0.5, hspace=0.5, height_ratios=[1, 2])

x2 = np.arange(0, 10, 0.1)
y2 = np.cos(x2)

axis10 = fig7.add_subplot(spec1[1])
axis10.plot(x2, y2)

axis11 = fig7.add_subplot(spec1[3])
axis11.plot(x2, y2)

plt.show()


print("-------------------------------------------------------------")

# importing required libraries
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

# create a figure
fig = plt.figure()

# to change size of subplot's
# set height of each subplot as 8
fig.set_figheight(8)

# set width of each subplot as 8
fig.set_figwidth(8)

# create grid for different subplots
spec = gridspec.GridSpec(ncols=2, nrows=2,
						width_ratios=[2, 1], wspace=0.5,
						hspace=0.5, height_ratios=[1, 2])

# initializing x,y axis value
x = np.arange(0, 10, 0.1)
y = np.cos(x)

# ax0 will take 0th position in
# geometry(Grid we created for subplots),
# as we defined the position as "spec[0]"
ax0 = fig.add_subplot(spec[0])
ax0.plot(x, y)

# ax1 will take 0th position in
# geometry(Grid we created for subplots),
# as we defined the position as "spec[1]"
ax1 = fig.add_subplot(spec[1])
ax1.plot(x, y)

# ax2 will take 0th position in
# geometry(Grid we created for subplots),
# as we defined the position as "spec[2]"
ax2 = fig.add_subplot(spec[2])
ax2.plot(x, y)

# ax3 will take 0th position in
# geometry(Grid we created for subplots),
# as we defined the position as "spec[3]"
ax3 = fig.add_subplot(spec[3])
ax3.plot(x, y)

# display the plots
plt.show()


print("-------------------------------------------------------------")

import matplotlib.pyplot as plt
import numpy as np

fig8, axis12 = plt.subplots(nrows=2,ncols=2,figsize=(7,7),gridspec_kw={
    'width_ratios':[3,3],
    'height_ratios':[3,3],
    'wspace':0.4,
    'hspace':0.4
})

x4 = np.arange(0,10,0.1)
y4 = np.tan(x4)

axis12[0][0].plot(x4,y4,color='blue')
axis12[0][1].plot(x4,y4,color='gold')
axis12[1][0].plot(x4,y4,color='green')
axis12[1][1].plot(x4,y4,color='red')


plt.show()


print("-------------------------------------------------------------")


import matplotlib.pyplot as plt
import numpy as np

fig9 = plt.figure()
fig.set_figheight(6)
fig9.set_figwidth(6)
axis13 = plt.subplot2grid(shape=(3,3), loc=(0,0), colspan=3)
axis14 = plt.subplot2grid(shape=(3,3), loc=(1,0), colspan=1)
axis15 = plt.subplot2grid(shape=(3,3), loc=(1,2), rowspan=2)
axis16 = plt.subplot2grid((3,3),(2,0))
axis17 = plt.subplot2grid((3,3),(2,1),colspan=1)

x5 = np.arange(0,10,0.1)
y5 = np.cos(x5)

axis13.plot(x5,y5)
axis13.set_title('axis13')

axis14.plot(x5,y5)
axis14.set_title('axis14')

axis15.plot(x5,y5)
axis15.set_title('axis15')

axis16.plot(x5,y5)
axis16.set_title('axis16')

axis17.plot(x5,y5)
axis17.set_title('axis17')

plt.tight_layout()
plt.show()

print("-------------------------------------------------------------")


import matplotlib.pyplot as plt
import numpy as np

fig8, axis12 = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), gridspec_kw={
    'width_ratios': [3, 3],
    'height_ratios': [3, 3],
    'wspace': 0.4,
    'hspace': 0.4
})

x4 = np.arange(0, 10, 0.1)
y4 = np.tan(x4)

axis12[0][0].plot(x4, y4, color='blue')
axis12[0][1].plot(x4, y4, color='gold')
axis12[1][0].plot(x4, y4, color='green')
axis12[1][1].plot(x4, y4, color='red')


plt.show()
