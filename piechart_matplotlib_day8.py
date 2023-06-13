"""
Plot a pie chart in Python using Matplotlib

A Pie Chart is a circular statistical plot that can display only one series of data. The area of the chart is the total percentage of the given data. The area of slices of the pie represents the percentage of the parts of the data. The slices of pie are called wedges. The area of the wedge is determined by the length of the arc of the wedge. The area of a wedge represents the relative percentage of that part with respect to whole data. Pie charts are commonly used in business presentations like sales, operations, survey results, resources, etc as they provide a quick summary.
 
Creating Pie Chart
Matplotlib API has pie() function in its pyplot module which create a pie chart representing the data in an array. 
 
Syntax: matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)
Parameters: 
data represents the array of data values to be plotted, the fractional area of each slice is represented by data/sum(data). If sum(data)<1, then the data values returns the fractional area directly, thus resulting pie will have empty wedge of size 1-sum(data). 
labels is a list of sequence of strings which sets the label of each wedge. 
color attribute is used to provide color to the wedges. 
autopct is a string used to label the wedge with their numerical value. 
shadow is used to create shadow of wedge. 
"""
import numpy as np
import matplotlib.pyplot as plt

name1 = ['Momo','Chowmin','Hotpot','Burger','Fried rice']
data1 = [70,60,80,40,50]
fig1 = plt.figure(figsize=(7,5))
plt.pie(data1,labels=name1)
plt.show()


"""
Customizing Pie Chart
A pie chart can be customized on the basis several aspects. The startangle attribute rotates the plot by the specified degrees in counter clockwise direction performed on x-axis of pie chart. shadow attribute accepts boolean value, if its true then shadow will appear below the rim of pie. Wedges of the pie can be customized using wedgeprop which takes Python dictionary as parameter with name values pairs denoting the wedge properties like linewidth, edgecolor, etc. By setting frame=True axes frame is drawn around the pie chart.autopct controls how the percentages are displayed on the wedges. 
"""

import numpy as np
import matplotlib.pyplot as plt

name1 = ['Momo', 'Chowmin', 'Hotpot', 'Burger', 'Fried rice']
data1 = [70, 60, 80, 40, 50]
colors = ['gold', 'red', 'blue', 'purple', 'black']
explode = (0.1, 0.4, 0.2, 0.0, 0.1)
wp1 = {'linewidth': 1, 'edgecolor': 'green'}


def func1(pct, values):
    absolute = int(pct / 100. * np.sum(values))
    return "{:.1f}%\n({:d}g)".format(pct, absolute)


fig1, axis1 = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = axis1.pie(data1,
                                    autopct=lambda pct: func1(pct, data1),
                                    explode=explode,
                                    labels=name1,
                                    shadow=True,
                                    colors=colors,
                                    startangle=90,
                                    wedgeprops=wp1,
                                    textprops=dict(color="magenta")
                                    )
axis1.legend(wedges, name1,
             title="Foods",
             loc="center left",
             bbox_to_anchor=(1, 0, 0.5, 1)
             )
plt.setp(autotexts, size=8, weight='bold')
axis1.set_title("Momo - pie chart customize")
plt.show()


"""
Creating a Nested Pie Chart
"""
"""
import matplotlib.pyplot as plt
import numpy as np

size = 5
name3 = ['Momo', 'Chowmin', 'Hotpot', 'Burger', 'Fried rice']
data3 = np.array([[70,50], [60,40], [80,30], [40,20],[50,30]])
norm3 = data3/np.sum(data3)*2*np.pi
left = np.cumsum(np.append(0,norm3.flatten()[:-1])).reshape(data3.shape)

#color scale
cmap3 = plt.get_cmap("tab20c")
outer_color3 = cmap3(np.arange(6)*4)
inner_color3 = cmap3(np.array([1, 2, 5, 6, 9,
                              10, 12, 13, 15,
                              17]))

#plot creation
fig3 , axis3 = plt.subplots(figsize=(9,6))

axis3.bar(x=left[:,0],
          width=norm3.sum(axis=1),
          bottom=1-size,
          height=size,
          color=outer_color3,
          edgecolor='w',
          linewidth=1,
          align='edge'
          )

axis3.bar(x=left.flatten(),
          width=norm3.flatten(),
          height=size,
          color=inner_color3,
          edgecolor='w',
          linewidth=1,
          align='edge'
          )

axis3.set(title='Nested Pie chart')
axis3.set_axis_off()

plt.show()
"""


# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
size = 5
cars = ['Momo', 'Chowmin', 'Hotpot', 'Burger', 'Fried rice']

data = np.array([[70,50], [60,40], [80,30], [40,20],[50,30]])
colors = ['gold', 'red', 'blue', 'purple', 'black']

# normalizing data to 2 pi
norm = data / np.sum(data)*2 * np.pi

# obtaining ordinates of bar edges
left = np.cumsum(np.append(0,
						norm.flatten()[:-1])).reshape(data.shape)

# Creating color scale
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(6)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9,
							10, 12, 13, 15,
							17, 18, 20 ]))

# Creating plot
fig, ax = plt.subplots(figsize =(10, 7),
					subplot_kw = dict(polar = True))

ax.bar(x = left[:, 0],
	width = norm.sum(axis = 1),
	bottom = 1-size,
	height = size,
	color = colors,
	edgecolor ='w',
	linewidth = 1,
	align ="edge")

ax.bar(x = left.flatten(),
	width = norm.flatten(),
	bottom = 1-2 * size,
	height = size,
	color = inner_colors,
	edgecolor ='w',
	linewidth = 1,
	align ="edge")

ax.set(title ="Nested pie chart")
ax.set_axis_off()

# show plot
plt.show()


"""
How to set border for wedges in Matplotlib pie chart?

Pie charts can be used for relative comparison of data. Python offers several data visualization libraries to work with. The Matplotlib library offers different types of graphs and inbuild methods and properties to manipulate the graph. The wedges in the pie chart can be given a border using the wedgeprops attribute of the pie() method of matplotlib.pyplot. Given below are two such examples to set a border to the wedges of the pie chart.

Syntax: wedgeprops : [dict | None]

Parameters:

dict: It is the property and its value. Example: {‘linewidth’:2} or {‘edgecolor’:’black’}
"""

"""
import matplotlib.pyplot as plt
import numpy as np

size = 5
name3 = ['Momo', 'Chowmin', 'Hotpot', 'Burger', 'Fried rice']
data3 = np.array([[70,50], [60,40], [80,30], [40,20],[50,30]])
norm3 = data3/np.sum(data3)*2*np.pi
left = np.cumsum(np.append(0,norm3.flatten()[:-1])).reshape(data3.shape)

#color scale
cmap3 = plt.get_cmap("tab20c")
outer_color3 = cmap3(np.arange(6)*4)
inner_color3 = cmap3(np.array([1, 2, 5, 6, 9,
                              10, 12, 13, 15,
                              17]))

#plot creation
fig3 , axis3 = plt.subplots(figsize=(9,6))

axis3.bar(x=left[:,0],
          width=norm3.sum(axis=1),
          bottom=1-size,
          height=size,
          color=outer_color3,
          edgecolor='w',
          linewidth=1,
          align='edge'
          )

axis3.bar(x=left.flatten(),
          width=norm3.flatten(),
          height=size,
          color=inner_color3,
          edgecolor='w',
          linewidth=1,
          align='edge'
          )

axis3.set(title='Nested Pie chart')
axis3.set_axis_off()

plt.show()
"""


# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
size = 5
cars = ['Momo', 'Chowmin', 'Hotpot', 'Burger', 'Fried rice']

data = np.array([[70,50], [60,40], [80,30], [40,20],[50,30]])
colors = ['gold', 'red', 'blue', 'purple', 'black']

# normalizing data to 2 pi
norm = data / np.sum(data)*2 * np.pi

# obtaining ordinates of bar edges
left = np.cumsum(np.append(0,
						norm.flatten()[:-1])).reshape(data.shape)

# Creating color scale
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(6)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9,
							10, 12, 13, 15,
							17, 18, 20 ]))

# Creating plot
fig, ax = plt.subplots(figsize =(10, 7),
					subplot_kw = dict(polar = True))

ax.bar(x = left[:, 0],
	width = norm.sum(axis = 1),
	bottom = 1-size,
	height = size,
	color = colors,
	linewidth = 1,
    edgecolor = 'black',
	align ="edge")

ax.bar(x = left.flatten(),
	width = norm.flatten(),
	bottom = 1-2 * size,
	height = size,
	color = inner_colors,
	edgecolor ='green',
	linewidth = 1,
	align ="edge")

ax.set(title ="Nested pie chart")
ax.set_axis_off()

# show plot
plt.show()
