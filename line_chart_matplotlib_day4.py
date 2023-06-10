"""
Line chart in Matplotlib – Python

Matplotlib is a data visualization library in Python. The pyplot, a sublibrary of matplotlib, is a collection of functions that helps in creating a variety of charts.  Line charts are used to represent the relation between two data X and Y on a different axis. Here we will see some of the examples of a line chart in Python :

Simple line plots
First import Matplotlib.pyplot library for plotting functions. Also, import the Numpy library as per requirement. Then define data values x and y. 
"""
"""import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([2, 8])
y1 = x1*2
plt.xlabel("x-axis")
plt.ylabel("x-axis")
plt.title("X-axis vs Y-axis")
plt.plot(x1, y1, color='red')
plt.show()"""
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([2, 8])
y_values = x1 * 2

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x1, y_values, color='red')
plt.show()

print("----------------------------------------------")

import matplotlib.pyplot as plt
import numpy as np

x2 = np.array([1, 2, 3, 4])
y2 = x2*2

plt.plot(x2, y2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show() 

plt.figure()
x2_2 = [2, 4, 6, 8]
y2_2 = [3, 5, 7, 9]
plt.plot(x2_2, y2_2, '-.')

plt.show()
print("----------------------------------------------")

import matplotlib.pyplot as plt
import numpy as np

x2 = np.array([1, 2, 3, 4])
y2 = x2*2

plt.plot(x2, y2)

x2_2 = [2, 4, 6, 8]
y2_2 = [3, 5, 7, 9]
plt.plot(x2_2, y2_2, '-.')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
print("----------------------------------------------")
import matplotlib.pyplot as plt
import numpy as np

x3_1 = np.array([1, 2, 3, 4])
y3_1 = x3_1*2

plt.plot(x3_1, y3_1)

x3_2 = [2, 4, 6, 8]
y3_2= [3, 5, 7, 9]

plt.plot(x3_1, y3_2)
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")

plt.fill_between(x3_1, y3_1, y3_2, color='gold', alpha=0.5)
plt.show()
print("----------------------------------------------")

"""
Line plot styles in Matplotlib

Python is a high-level, interpreted, and dynamically typed programming language that can be used to manage huge datasets. Python supports a wide variety of data visualization libraries like Matplotlib, Seaborn, Bokeh, Geoplotlib, Ggplot, and Plotly. Among all these libraries, Matplotlib is comparatively simple and easy to implement. The Matplotlib library of Python is a popular choice for data visualization due to its wide variety of chart types and its properties that can be manipulated to create chart styles. The matplotlib.pyplot.plot(*args, **kwargs) method of matplotlib.pyplot is used to plot the graph and specify the graph style like color or line style. 

The following line styles are available in Matplotlib:
The following examples demonstrate plotting graphs having different line styles:

Example 1:

In this example, the matplotlib.pyplot library is imported. The student names are added to the student’s list and the marks list is created at the random.randint() method. Next, the X and Y axis are labeled and the graph is given a title. Finally, the graph is plotted using the plot() method of matplotlib.pyplot. Here the abbreviated form of color and line style is used. The color abbreviation chosen is ‘m’ which is magenta and the line style chosen is ‘–‘ which is dashed line style.

Below is the implementation
"""

import random as rn
import matplotlib.pyplot as plt

students = ["Jane","Joe","Beck","Tom",
            "Sam","Eva","Samuel","Jack",
            "Dana","Ester","Carla","Steve",
            "Fallon","Liam","Culhane","Candance",
            "Ana","Mari","Steffi","Adam"]
marks = []
for i in range(0,len(students)):
    marks.append(rn.randint(0,100))

plt.xlabel("Students",fontsize=20)
plt.ylabel("Marks")
plt.plot(students,marks,'--',color='gold')
plt.show()

print("----------------------------------------------")
import random as rn
import matplotlib.pyplot as plt

students = ["Jane","Joe","Beck","Tom",
            "Sam","Eva","Samuel","Jack",
            "Dana","Ester","Carla","Steve",
            "Fallon","Liam","Culhane","Candance",
            "Ana","Mari","Steffi","Adam"]
marks = []
for i in range(0,len(students)):
    marks.append(rn.randint(0,100))

plt.xlabel("Students",fontsize=20)
plt.ylabel("Marks")
plt.plot(students,marks,'--',color='gold',marker='o',markerfacecolor='lime')
plt.show()

print("----------------------------------------------")
import matplotlib.pyplot as plt

x4 = [10,30,50]
y4 = [20,20,20]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(y4,x4)
plt.title("X-Y axis")
plt.show()


print("----------------------------------------------")

"""
Plotting Multiple Lines
In this example, we will learn how to draw multiple lines with the help of matplotlib. Here we will use two lists as data with two dimensions (x and y) and at last plot the lines as different dimensions and functions over the same data.

To draw multiple lines we will use different functions which are as follows:

y = x
x = y
y = sin(x)
y = cos(x)
"""
import matplotlib.pyplot as plt
import numpy as np
x4 = [1, 2, 3, 4, 5]
y4 = [3, 3, 3, 3, 3]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(y4, x4, label='line-1')
plt.plot(x4, y4, label='line-2')
plt.plot(np.sin(x4),'--' ,label='Sin-curve-1')
plt.plot(np.cos(x4), '--' ,label='Cos-curve-1')
plt.plot(np.sin(y4), label='Sin-curve-2')
plt.plot(np.cos(y4), label='Cos-curve-2')
plt.title("X-Y axis")
plt.show()

print("----------------------------------------------")
"""
Plotting Multiple Lines with different Line styles
This example is similar to the above example and the enhancement is the different line styles. This can help in the modification of better visualization. 

Here we will use different line styles which are as follows:

–        : dashed
—      : double dashed
-.       : dashed-dotted
:        : dotted
"""
# importing package
import matplotlib.pyplot as plt
import numpy as np

# create data
x = [1,2,3,4,5]
y = [3,3,3,3,3]

# plot lines
plt.plot(x, y, label = "line 1", linestyle="-")
plt.plot(y, x, label = "line 2", linestyle="--")
plt.plot(x, np.sin(x), label = "curve 1", linestyle="-.")
plt.plot(x, np.cos(x), label = "curve 2", linestyle=":")
plt.legend()
plt.show()

print("----------------------------------------------")

"""
Change the line opacity in Matplotlib

In this article, we will learn how to Create the line opacity in Matplotlib. Let’s discuss some concepts :

A line chart or line graph may be a sort of chart which displays information as a series of knowledge points called ‘markers’ connected by line segments. Line graphs are usually wont to find relationships between two data sets on the different axis; as example X, Y.
Matplotlib allows you to regulate the transparency of a graph plot using the alpha attribute.
By default, alpha=1.
If you would like to form the graph plot more transparent, then you’ll make alpha but 1, such as 0.5 or 0.25.
If you would like to form the graph plot less transparent, then you’ll make alpha greater than 1. This solidifies the graph plot, making it less transparent and more thick and dense, so to talk .
Approach:

Import Library (Matplotlib)
Import / create data.
Plot a graph (line) with opacity.
Example 1: (Simple line graph with its opacity)
"""
import matplotlib.pyplot as plt
import numpy as np
x4 = [1, 2, 3, 4, 5]
y4 = [3, 3, 3, 3, 3]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(y4, x4, label='line-1')
plt.plot(x4, y4, label='line-2')
plt.plot(np.sin(x4),'--' ,label='Sin-curve-1')
plt.plot(np.cos(x4), '--' ,label='Cos-curve-1')
plt.plot(np.sin(y4), label='Sin-curve-2')
plt.plot(np.cos(y4), label='Cos-curve-2')
plt.title("X-Y axis")
plt.show()

print("----------------------------------------------")
"""
Change the line opacity in Matplotlib

In this article, we will learn how to Create the line opacity in Matplotlib. Let’s discuss some concepts :

A line chart or line graph may be a sort of chart which displays information as a series of knowledge points called ‘markers’ connected by line segments. Line graphs are usually wont to find relationships between two data sets on the different axis; as example X, Y.
Matplotlib allows you to regulate the transparency of a graph plot using the alpha attribute.
By default, alpha=1.
If you would like to form the graph plot more transparent, then you’ll make alpha but 1, such as 0.5 or 0.25.
If you would like to form the graph plot less transparent, then you’ll make alpha greater than 1. This solidifies the graph plot, making it less transparent and more thick and dense, so to talk .
Approach:

Import Library (Matplotlib)
Import / create data.
Plot a graph (line) with opacity.
Example 1: (Simple line graph with its opacity)
"""
# importing libraries
import matplotlib.pyplot as plt

# create data
x5 = [1, 2, 3, 4, 5]
y5 = x5

# plot the graph
plt.plot(x5, y5, linewidth=10, alpha=1.0)
x6 = [2,4,6,8,10]
y6 = x6
plt.plot(x6,y6,linewidth= 10,alpha=0.2)
plt.show()

print("----------------------------------------------")
x7 = np.array([-2,-1,0,1,2])
y7_1 = x7*0
y7_2 = x7*x7
y7_3 = -x7*x7
plt.plot(x7,y7_1,alpha=0.5,color='red')
plt.plot(x7,y7_2,alpha=0.3,color='lime')
plt.plot(x7,y7_3,alpha=1,color='gold')
plt.legend(["op=0.5","op=0.3","op=1"])
plt.show()

print("----------------------------------------------")
# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
#x = [1, 2, 3, 4, 5]

# plot
for i in range(10):
	plt.plot([1, 2.8], [i]*2, linewidth=5, color='red', alpha=0.1*i)
	plt.plot([3.1, 4.8], [i]*2, linewidth=5, color='lime', alpha=0.1*i)
	plt.plot([5.1, 6.8], [i]*2, linewidth=5, color='gold', alpha=0.1*i)
	plt.plot([7.1, 8.8], [i]*2, linewidth=5, color='blue', alpha=0.1*i)
	
for i in range(10):
	plt.plot([1, 2.8], [-i]*2, linewidth=5, color='red', alpha=0.1*i)
	plt.plot([3.1, 4.8], [-i]*2, linewidth=5, color='lime', alpha=0.1*i)
	plt.plot([5.1, 6.8], [-i]*2, linewidth=5, color='gold', alpha=0.1*i)
	plt.plot([7.1, 8.8], [-i]*2, linewidth=5, color='blue', alpha=0.1*i)
	
plt.show()


print("----------------------------------------------")
"""
Increase the thickness of a line with Matplotlib

Prerequisites: Matplotlib

Matplotlib is the most widely used library for plotting graphs with the available dataset. Matplotlib supports line chart which are used to represent data over a continuous time span. In line chart, the data value is plotted as points and later connected by a line to show trend of a measure over time. The functionality of increasing the thickness of a line is given by linewidth attribute.

Linewidth: By default the linewidth is 1. For graphs with multiple lines it becomes difficult to trace the lines with lighter colors. This situation can be handled by increasing the linewidth. The linewidth can be used to focus on certain data compared to the others. It can help get a detailed visualization of the particular record in the dataset. This attribute belongs to plot function().

Approach
Import modules
Create or load data
Plot graph with required line thickness
Display plot
Functions used
xlabel()- This function is used to set labels for x-axis
Syntax: plt.xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)


Parameter:

xlabel: accepts string type value and is used to label the X axis.
fontdict: used to override default font properties of the label. Its default value is None and is optional.
labelpad: default value is None. It is used to specify the spacing of the label from the axes. This is optional.
**kwargs: used to specify other properties that can be used to modify the appearance of the label.
ylabel()- this function is used to set labels for y-axis
Syntax: plt.ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)

Parameter:

ylabel: accepts string type value and is used to label the Y axis.
fontdict: used to override default font properties of the label. Its default value is None and is optional.
labelpad: default value is None. It is used to specify the spacing of the label from the axes. This is optional.
**kwargs: used to specify other properties that can be used to modify the appearance of the label.
plot()- It is used to make a 2D hexagonal binning plot of points x, y.
Syntax: plt.plot(x,y, data=None, **kwargs)

Parameter

x,y : used to specify the data to be plotted along the x and y axis.
data: default value is None. It is an object with labelled data and can be passed instead of the x,y values. If data object is passed then the xand y label should be specified.
**kwargs: used to specify line properties like linewidth, color, antialiasing, marker, markercolor etc.
legend()- A legend is an area describing the elements of the graph. In the matplotlib library, there’s a function called legend() which is used to Place a legend on the axes.
Syntax: plt.legend(**options)

Parameter

**options: used to specify the properties of the legend, its size, its location, edgecolor, facecolor etc
"""

import matplotlib.pyplot as plt

places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
literacy_rate = [100, 98, 90, 85, 75, 50, 30, 45, 65, 70]
female_literacy = [95, 100, 50, 60, 85, 80, 75, 99, 70, 30]

plt.xlabel("Places")
plt.ylabel("Percentage")

plt.plot(places, literacy_rate, color='red', label='literacy_rate')
plt.plot(places, female_literacy, color='lime', label='female_literacy')
plt.legend(loc='lower left', ncol=1)

plt.show()


print("----------------------------------------------")
import matplotlib.pyplot as plt

places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
literacy_rate = [100, 98, 90, 85, 75, 50, 30, 45, 65, 70]
female_literacy = [95, 100, 50, 60, 85, 80, 75, 99, 70, 30]

plt.xlabel("Places")
plt.ylabel("Percentage")

plt.plot(places, literacy_rate, color='red',linestyle='dotted',label='literacy_rate',marker='o',markerfacecolor='gold')
plt.plot(places, female_literacy, color='lime', label='female_literacy',marker='*',markerfacecolor='white')
plt.title("Places vs Percentage graph")
plt.legend(loc='lower left', ncol=1)

plt.show()

print("----------------------------------------------")

"""
How to Fill Between Multiple Lines in Matplotlib?

With the use of the fill_between()  function in the Matplotlib library in Python, we can easily fill the color between any multiple lines or any two horizontal curves on a 2D plane.

Syntax: matplotlib.pyplot.fill_between(x, y1, y2=0, where=None, step=None, interpolate=False, *, data=None, **kwargs)

"""

import pylab as pl
import numpy as np

x8 = np.arange(0,2,0.01)
y8_1 = np.sin(2*np.pi*x8)
y8_2 = 0.8*np.sin(4*np.pi*x8)

fig8, (axis8_1,axis8_2,axis8_3) = plt.subplots(3,1,sharex=True, figsize=(6,6))

axis8_1.fill_between(x8,y8_1)
axis8_1.set_title("fillling between Y8_1 and 0")
axis8_2.fill_between(x8,y8_1,1)
axis8_2.set_title("fillling between Y8_1 and 1")
axis8_3.fill_between(x8,y8_1,y8_2)
axis8_3.set_title("fillling between Y8_1 and y8_2")

axis8_3.set_xlabel("X")
fig8.tight_layout()


print("----------------------------------------------")

x9 = np.linspace(0,3,200)
Y9_1 = x9**2 + 3
Y9_2 = np.sin(x9)
Y9_3 = np.cos(x9)

plt.plot(x9, Y9_1, lw=4)
plt.plot(x9, Y9_2, lw=4)
plt.plot(x9, Y9_3, lw=4)
 
plt.fill_between(x9, Y9_1, Y9_2, color='k', alpha=.5)
plt.fill_between(x9, Y9_1, Y9_3, color='y', alpha=.5)

plt.show()

print("----------------------------------------------")

import matplotlib.pyplot as plt


x11 = [1, 2, 1, 0]
y11 = [2, 1, 0, 1]

plt.fill(x11, y11)
plt.show()


print("----------------------------------------------")

import matplotlib.pyplot as plt

x10 = [4,6,8,10]
y10 = [6,4,10,8]

plt.fill(x10,y10)
plt.show()