"""
Matplotlib.pyplot.legend() in Python

Matplotlib is one of the most popular Python packages used for data visualization. It is a cross-platform library for making 2D plots from data in arrays. Pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

Matplotlib.pyplot.legend()
A legend is an area describing the elements of the graph. In the matplotlib library, there’s a function called legend() which is used to Place a legend on the axes.

The attribute Loc in legend() is used to specify the location of the legend.Default value of loc is loc=”best” (upper left). The strings ‘upper left’, ‘upper right’, ‘lower left’, ‘lower right’ place the legend at the corresponding corner of the axes/figure.

The attribute bbox_to_anchor=(x, y) of legend() function is used to specify the coordinates of the legend, and the attribute ncol represents the number of columns that the legend has.It’s default value is 1.


Syntax:

matplotlib.pyplot.legend([“blue”, “green”], bbox_to_anchor=(0.75, 1.15), ncol=2)

The Following are some more attributes of function legend() :

shadow: [None or bool] Whether to draw a shadow behind the legend.It’s Default value is None.
markerscale: [None or int or float] The relative size of legend markers compared with the originally drawn ones.The Default is None.
numpoints: [None or int] The number of marker points in the legend when creating a legend entry for a Line2D (line).The Default is None.
fontsize: The font size of the legend.If the value is numeric the size will be the absolute font size in points.
facecolor: [None or “inherit” or color] The legend’s background color.
edgecolor: [None or “inherit” or color] The legend’s background patch edge color.
Ways to use legend() function in Python –
Example 1:
"""

import numpy as np
import matplotlib.pyplot as plt

#x-axis value
x1 = [3,7,2,5]
#y-axis value
y1 = [3,4,1,9]

plt.plot(x1,y1,color='green')

plt.legend("Plotting a single graph",loc='upper left')

plt.show()

print("------------------------------------")

import numpy as np
import matplotlib.pyplot as plt

plt.plot(x1,label='x-axis',color='red')
plt.plot(y1,label='y-axis',color='blue')

plt.legend(loc='upper left')

plt.show()
print("------------------------------------")
import numpy as np
import matplotlib.pyplot as plt

x2 = np.arange(0, 10, 0.1)  
fig2, axis2 = plt.subplots()

axis2.plot(x2, np.sin(x2), 'blue', label='sine wave')
axis2.plot(x2, np.cos(x2), linestyle='dotted',color='red', label='cos wave')

axis2.axis('equal')
leg1 = axis2.legend(loc='upper left')
plt.show()
print("------------------------------------")

import numpy as np
import matplotlib.pyplot as plt
 
x3 = [1,3,5,7]
y3_1 = [2,4,6,8]
y3_2 = [3,5,7,9]

plt.plot(y3_1, label='y=x',color='green')
plt.plot(y3_2, label='y=3x')

plt.legend(bbox_to_anchor=(0.75,1.15),ncol=2)

plt.show()
print("------------------------------------")
"""
Matplotlib.axes.Axes.legend() in Python

Matplotlib is a library in Python and it is numerical – mathematical extension for NumPy library. The Axes Class contains most of the figure elements: Axis, Tick, Line2D, Text, Polygon, etc., and sets the coordinate system. And the instances of Axes supports callbacks through a callbacks attribute.

matplotlib.axes.Axes.legend() Function
The Axes.legend() function in axes module of matplotlib library is used to place a legend on the axes.

Syntax: Axes.legend(self, *args, **kwargs)

Parameters: This method accepts the following parameters.


labels : This parameter is the list of labels to show next to the artists.
handles : This parameter is the list of Artists (lines, patches) to be added to the legend.
Returns:This method returns the matplotlib.legend.Legend instance.
"""

import matplotlib.pyplot as plt
fig4, axis4 = plt.subplots()

line4_1, = axis4.plot([2,4,6],
                    label='Line 1',
                    color='gold',
                    linewidth=3,
                    linestyle='dotted')
line_4_2, = axis4.plot([6,4,2],
                    label='Line 2',
                    color='red',
                    linewidth=3,
                    linestyle='solid')

fourth_legend = axis4.legend(handles=[line4_1],loc='upper center')
axis4.add_artist(fourth_legend)
axis4.legend(handles=[line_4_2],loc='lower center')

fig4.suptitle('Matplotlib.axes.Axes.legend()')

plt.show()

print("------------------------------------")

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(20570528)

fig5, axis5 = plt.subplots()
for color in ['gold', 'red', 'green']:
    n = 90
    x5, y5 = np.random.rand(2, n)
    scale = 1000.0 * np.random.rand(n)
    axis5.scatter(x5, y5, c=color, s=scale,
                  label=color,
                  alpha=0.35)
axis5.legend()
axis5.grid(True)
fig5.suptitle('Matplotlib.axes.Axes.legend() function', fontweight='bold')
plt.show()

print("------------------------------------")
