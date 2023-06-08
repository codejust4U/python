"""
Python | Introduction to Matplotlib

Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was introduced by John Hunter in the year 2002. One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data in easily digestible visuals. Matplotlib consists of several plots like line, bar, scatter, histogram etc. Installation : Windows, Linux and macOS distributions have matplotlib and most of its dependencies as wheel packages.
"""

"""
Basic plots in Matplotlib :
Matplotlib comes with a wide variety of plots. Plots helps to understand trends, patterns, and to make correlations. They’re typically instruments for reasoning about quantitative information. Some of the sample plots are covered here. Line plot : 
"""

from matplotlib import pyplot as plt
x = [1,3,5,7]
y = [2,4,6,8]
plt.plot(x,y)
plt.show()
print("-----------------------------------------------------------")
x1 = [5, 2, 9, 4, 7]
x2 = [10, 5, 8, 4, 2]
plt.plot(x1,x2)
plt.show()

print("-----------------------------------------------------------")

plt.bar(x,y)
plt.show()

print("-----------------------------------------------------------")

plt.hist(x1)
plt.show()

print("-----------------------------------------------------------")

plt.scatter(x1,x2)
plt.show()

print("-----------------------------------------------------------")

"""
Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python. Matplotlib can be used in Python scripts, the Python and IPython shell, web application servers, and various graphical user interface toolkits like Tkinter, awxPython, etc.
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()

print("-----------------------------------------------------------")

import matplotlib.pyplot as plt
d_year = [1972, 1982, 1992, 2002, 2012]
d_india = [100.6, 158.61, 305.54, 394.96, 724.79]
d_nepal = [12.5,23,56.78,112,298.56]
d_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

plt.plot(d_year,d_india, color = 'green',label='India')
plt.plot(d_year,d_nepal, color = 'Blue',label='Nepal')
plt.plot(d_year,d_bangladesh, color = 'red',label='Bangladesh')


plt.xlabel('Years')
plt.ylabel('Power Consumption in KWh')

plt.title('Electricity Consumption per Capital of India , Nepal and Bangladesh')

plt.legend()
plt.show()


print("-----------------------------------------------------------")

import matplotlib.pyplot as plt
d_year = [1972, 1982, 1992, 2002, 2012]
d_india = [100.6, 158.61, 305.54, 394.96, 724.79]
d_nepal = [12.5,23,56.78,112,298.56]
d_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

plt.plot(d_year,d_nepal,color='blue', marker = 'o', markersize = 12, label='Nepal')
plt.plot(d_year,d_india,color='green',linestyle='dashed',linewidth=2,label='India')
plt.plot(d_year,d_bangladesh,color='red',linestyle='dotted',linewidth=2,label='Bangladesh')

plt.xlabel('Years')
plt.ylabel('Power Consumption in KWh')

plt.title('Electricity consumption per Capita of Nepal, India and Bangladesh')

plt.legend()
plt.show()

print("-----------------------------------------------------------")

"""
Matplotlib – Axes Class

Matplotlib is one of the Python packages which is used for data visualization. You can use the NumPy library to convert data into an array and numerical mathematics extension of Python. Matplotlib library is used for making 2D plots from data in arrays.

Axes class
Axes is the most basic and flexible unit for creating sub-plots. Axes allow placement of plots at any location in the figure. A given figure can contain many axes, but a given axes object can only be in one figure. The axes contain two axis objects 2D as well as, three-axis objects in the case of 3D. Let’s look at some basic functions of this class.

axes() function
axes() function creates axes object with argument, where argument is a list of 4 elements [left, bottom, width, height]. Let us now take a brief look to understand the axes() function.
"""

fig1 = plt.figure()
axis1 = plt.axes([0.1,0.1,0.8,0.8])


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])

print("-----------------------------------------------------------")

"""
ax.legend() function
Adding legend to the plot figure can be done by calling the legend() function of the axes class. It consists of three arguments.

Syntax :

ax.legend(handles, labels, loc)
Where labels refers to a sequence of string and handles, a sequence of Line2D or Patch instances, loc can be a string or an integer specifying the location of legend.
"""

fig3 = plt.figure()
ax3 = plt.axes([0.1,0.1,0.8,0.8])

ax3.legend(labels = ('label1','label2'), loc = 'upper left')

print("-----------------------------------------------------------")

"""
ax.plot() function
plot() function of the axes class plots the values of one array versus another as line or marker.

Syntax : plt.plot(X, Y, ‘CLM’)

Parameters:
X is x-axis.
Y is y-axis.
‘CLM’ stands for Color, Line and Marker.

Note: Line can be of different styles such as dotted line (':'), dashed line ('—'), solid line ('-') and many more.

Marker codes

Characters	Description
‘.’	Point Marker
‘o’	Circle Marker
‘+’	Plus Marker
‘s’	Square Marker
‘D’	Diamond Marker
‘H’	Hexagon Marker
"""
import matplotlib.pyplot as plt
import numpy as np
data1 = np.linspace(-np.pi, np.pi, 15)
cos_val1 = np.cos(data1)
sin_val1 = np.sin(data1)

#ax4 = plt.axes([0.1,0.1,0.8,0.8])

#ax5 = ax4.plot(data1,cos_val1, 'bs: ')

#ax6 = ax4.plot(data1,sin_val1, 'ro-')
"""ax4.legend(labels=('Cosine Function', 'Sine Function'), loc='upper left')

ax4.set_title("Trignometric Functions")
plt.show()
"""
plt.plot(data1, cos_val1, 'bs:')
plt.plot(data1, sin_val1, 'ro-')
plt.legend(labels=('Cosine Function', 'Sine Function'), loc='upper left')
plt.title("Trigonometric Functions")
plt.show()

print("-----------------------------------------------------------")

"""
How to create multiple subplots in Matplotlib in Python?

To create multiple plots use matplotlib.pyplot.subplots method which returns the figure along with Axes object or array of Axes object. nrows, ncols attributes of subplots() method determine the number of rows and columns of the subplot grid.

By default, it returns a figure with a single plot. For each axes object i.e plot we can set title (set via set_title()), an x-label (set via set_xlabel()), and a y-label set via set_ylabel()).

Let’s see how this works  

When we call the subplots() method by stacking only in one direction it returns a 1D array of axes object i.e subplots.
We can access these axes objects using indices just like we access elements of the array. To create specific subplots, call matplotlib.pyplot.plot() on the corresponding index of the axes. Refer to the following figure for a better understanding

"""

arr1 = [2,4,6]
arr2 = [0,2,0]
arr3 = [2, 0,2]

fig4, ax5 = plt.subplots(2)

ax5[0].plot(arr1, arr2)
ax5[1].plot(arr1, arr3)

print("-----------------------------------------------------------")

arr4 = np.arange(0.0,2.0,0.01)
arr5 = 1+np.sin(2*np.pi*arr4)

fug5, ((ax6,ax7),(ax8,ax9),(ax10,ax11)) = plt.subplots(3,2)
ax6.plot(arr4,arr5,color='gold')
ax7.plot(arr4,arr5,color='green')
ax8.plot(arr4,arr5,color='blue')
ax9.plot(arr4,arr5,color='black')
ax10.plot(arr4,arr5,color='red')
ax11.plot(arr4,arr5,color='pink')

print("-----------------------------------------------------------")

