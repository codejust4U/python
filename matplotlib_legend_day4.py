"""
How to Place Legend Outside of the Plot in Matplotlib?

In this article, we will see how to put the legend outside the plot. 

Let’s discuss some concepts :

Matplotlib: Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was introduced by John Hunter in the year 2002.
Legend: A legend is an area describing the elements of the graph. In the Matplotlib library, there’s a function called legend() which is used to Place a legend on the axes. The attribute Loc in legend() is used to specify the location of the legend. The default value of loc is loc=  “best” (upper left).
Put the legend outside the plot
As, we can see that the above figure legends overlapped on the graph i.e; incomplete information. To solve this problem we need to place the legend outside the plot.

The syntax to set the legend outside is as given below:
matplotlib.pyplot.legend(bbox_to_anchor=(x,y))
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")


plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.show()

print('-------------------------------------------------')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")


plt.legend(bbox_to_anchor = (1.25, 0.6), loc='center right')
plt.tight_layout()
plt.show()

print('-------------------------------------------------')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")


plt.legend(bbox_to_anchor=(0.5, 1.2), loc='upper center')
plt.tight_layout()
plt.show()

print('-------------------------------------------------')

import numpy as np
import matplotlib.pyplot as plt

x_4 = np.linspace(-5,5,100)
colors = [['yellow','green'],['red','blue']]

fig4, axis4 = plt.subplots(2,2)
for i in range(2):
    axis4[0][i].plot(x_4, np.sin(x_4+i),
                     color=colors[0][i],
                     label='y=sin(x+{})'.format(i))
    axis4[1][i].plot(x_4, np.sin(x_4+i),
                     color=colors[1][i],
                     label='y=sin(x+{})'.format(i))

fig4.legend(bbox_to_anchor=(1.3,0.6))

fig4.tight_layout()
plt.show()

print('-------------------------------------------------')

"""

How to Remove the Legend in Matplotlib?

Matplotlib is one of the most popular data visualization libraries present in Python. Using this matplotlib library, if we want to visualize more than a single variable, we might want to explain what each variable represents. For this purpose, there is a function called legend() present in matplotlib library. This legend is a small area on the graph describing what each variable represents.

In order to remove the legend, there are four ways. They are : 

Using .remove()
Using .set_visible()
Fix legend_ attribute of the required Axes object = None
Using label=_nolegend_   
Method 1: Using .remove()

Example 1: By using ax.get_legend().remove() method, legend can be removed from figure in matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

x_5 = np.linspace(-3, 3, 100)
y5_1 = np.power(x, 2)
y5_2 = np.power(x, 3)

fig5, axis5 = plt.subplots()

axis5.plot(x_5, y5_1, c = 'r',label = 'x^2')
axis5.plot(x_5, y5_2, c = 'g',label = 'x^3')

leg = plt.legend()

axis5.get_legend().remove()

plt.show()

print('-------------------------------------------------')
import numpy as np
import matplotlib.pyplot as plt

x6 = np.linspace(-3, 3, 100)
y6_1 = np.power(x, 2)
y6_2 = np.power(x, 3)

fig6, axs6 = plt.subplots(2, 1)

axs6[0].plot(x6, y6_1, c = 'r',label = 'x^2')
axs6[1].plot(x6, y6_2, c = 'g',label = 'x^3')

axs6[0].legend(loc = 'upper left')
axs6[1].legend(loc = 'upper left')

axs6[0].get_legend().remove()
axs6[1].get_legend().remove()


plt.show()
print('-------------------------------------------------')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1,c = 'r',label = 'Sine')
ax.plot(x, y2,c = 'g',label = 'Cosine')

leg = plt.legend()

ax.get_legend().set_visible(False)

plt.show()
print('-------------------------------------------------')
x7 = np.linspace(1,10,100)
y7_1 = np.sin(x7)
y7_2 = np.cos(x7)

plt.plot(x7,y7_1)
plt.plot(x7,y7_2)
plt.legend(['Sine wave','Cos wave'])

plt.show()

print('-------------------------------------------------')

x7 = np.linspace(1,10,100)
y7_1 = np.sin(x7)
y7_2 = np.cos(x7)

plt.plot(x7,y7_1)
plt.plot(x7,y7_2)
plt.legend(['Sine wave','Cos wave'],frameon=False)

plt.show()

print('-------------------------------------------------')

x7 = np.linspace(1,10,100)
y7_1 = np.sin(x7)
y7_2 = np.cos(x7)

plt.plot(x7,y7_1)
plt.plot(x7,y7_2)
lab = plt.legend(['Sine wave','Cos wave'])

lab.get_frame().set_alpha(0)
plt.show()

print('-------------------------------------------------')