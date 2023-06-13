"""
matplotlib.pyplot.scatter() in Python

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is used for plotting various plots in Python like scatter plot, bar charts, pie charts, line plots, histograms, 3-D plots and many more. We will learn about the scatter plot from the matplotlib library. 
Note: For more information, refer to Python Matplotlib – An Overview
 

matplotlib.pyplot.scatter()
Scatter plots are used to observe relationship between variables and uses dots to represent the relationship between them. The scatter() method in the matplotlib library is used to draw a scatter plot. Scatter plots are widely used to represent relation among variables and how change in one affects the other. 
Syntax 
The syntax for scatter() method is given below:
 

matplotlib.pyplot.scatter(x_axis_data, y_axis_data, s=None, c=None, marker=None, cmap=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None) 
 

The scatter() method takes in the following parameters: 
 


x_axis_data- An array containing x-axis data
y_axis_data- An array containing y-axis data
s- marker size (can be scalar or array of size equal to size of x or y)
c- color of sequence of colors for markers
marker- marker style
cmap- cmap name
linewidths- width of marker border
edgecolor- marker border color
alpha- blending value, between 0 (transparent) and 1 (opaque)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(13)
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y, c="red",alpha=0.5)
plt.title("Scatter plot")
plt.show()

print("-------------------------------------------------")

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(13)
y1_1 = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]
y1_2 = [55, 87, 34, 23, 36, 55, 67, 98, 34, 65, 94, 11, 56]

plt.scatter(x1, y1_1, c="red", alpha=0.5)

plt.scatter(x1, y1_2, c="gold", alpha=0.5, marker='^')
plt.title("Scatter plot")
plt.show()

print("-------------------------------------------------")

"""
How to add a legend to a scatter plot in Matplotlib ?

In this article, we are going to add a legend to the depicted images using matplotlib module. We will use the matplotlib.pyplot.legend() method to describe and label the elements of the graph and distinguishing different plots from the same graph. 

Syntax: matplotlib.pyplot.legend( [“title_1”, “Title_2”],  ncol = 1 , loc = “upper left” ,bbox_to_anchor =(1, 1) )

Parameters :

ncol: [takes int, optional parameter] the default value is 1. It represents the number of columns in legend.
loc: [takes string, optional parameter] the default value is “best” i.e “upper left”. It represents the location of the legend. Other options can be: “best”, “upper right”, “upper left”, “lower left”, “lower right” , “right”, “center left”, “center right”, “lower center”, “upper center”, “center”.
bbox_to_anchor: [takes a list or tuple of 2 int/float, optional parameter ]. It represents the co-ordinates of legend on the graph. Both x and y co-ordinates are mandatory to give.
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(13)
y1_1 = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]
y1_2 = [55, 87, 34, 23, 36, 55, 67, 98, 34, 65, 94, 11, 56]

plt.scatter(x1, y1_1, c="red", alpha=0.5)

plt.scatter(x1, y1_2, c="gold", alpha=0.5, marker='^')
plt.title("Scatter plot")
plt.legend(['X1 vs Y1_1','X2 vs Y2_2'],loc='upper left')
plt.show()

print("-------------------------------------------------")

"""
How to Connect Scatterplot Points With Line in Matplotlib?

Prerequisite: Scatterplot using Seaborn in Python

Scatterplot can be used with several semantic groupings which can help to understand well in a graph. They can plot two-dimensional graphics that can be enhanced by mapping up to three additional variables while using the semantics of hue, size, and style parameters. And matplotlib is very efficient for making 2D plots from data in arrays. In this article, we are going to see how to connect scatter plot points with lines in matplotlib.

Approach:

Import module.
Determined X and Y coordinate for plot scatter plot points.
Plot scatterplot.
Plot matplotlib.pyplot with the same X and Y coordinate.
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(13)
y1_1 = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]
y1_2 = [55, 87, 34, 23, 36, 55, 67, 98, 34, 65, 94, 11, 56]

plt.scatter(x1,y1_1,color='lime',alpha=.6)
plt.plot(x1,y1_1)
plt.scatter(x1,y1_2,color='black',alpha=.6)
plt.plot(x1,y1_2)
plt.show()


print("-------------------------------------------------")

"""
How to create a Scatter Plot with several colors in Matplotlib?

Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python. Matplotlib can be used in Python scripts, the Python and IPython shell, web application servers, and various graphical user interface toolkits like Tkinter, awxPython, etc.

In-order to create a scatter plot with several colors in matplotlib, we can use the various methods:

Using the parameter marker color to create a Scatter Plot 
The possible values for marker color are:

A single color format string.
A 2-D array in which the rows are RGB or RGBA.
"""

# import required modules
import matplotlib.pyplot as plt
import numpy as np

# assign data points
a = np.array([[9, 1, 2, 7, 5, 8, 3, 4, 6],
				[4, 2, 3, 7, 9, 1, 6, 5, 8]])

# assign categories
categories = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])

# use colormap
colormap = np.array(['r', 'g', 'b'])

# depict illustration
plt.scatter(a[0], a[1], s=100, c=colormap[categories])
plt.plot(a[0],a[1])
plt.show()

print("-------------------------------------------------")

"""
How to increase the size of scatter points in Matplotlib ?

Prerequisites: Matplotlib

Scatter plots are the data points on the graph between x-axis and y-axis in matplotlib library. The points in the graph look scattered, hence the plot is named as ‘Scatter plot’. The points in the scatter plot are by default small if the optional parameters in the syntax are not used. The optional parameter ‘s’ is used to increase the size of scatter points in matplotlib. Discussed below are various ways in which s can be set.

Syntax :

matplotlib.pyplot.scatter(x_axis_data, y_axis_data, s=None, c=None, marker=None, cmap=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None)


Parameters:

x_axis_data- An array containing x-axis data
y_axis_data- An array containing y-axis data
s- marker size (can be scalar or array of size equal to size of x or y)
c- color of sequence of colors for markers
marker– marker style
cmap- cmap name
linewidths- width of marker border
edgecolor- marker border color
alpha- blending value, between 0 (transparent) and 1 (opaque)

"""

import numpy as np
import matplotlib.pyplot as plt

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = [8, 7, 6, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x3,y3,color='gold',s=100)

plt.show()


print("-------------------------------------------------")

"""Data points in scatter plot with variable size"""

import numpy as np
import matplotlib.pyplot as plt

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
points3 = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(x3,y3,color='lime',s=points3)

plt.show()