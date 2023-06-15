"""
Tri-Surface Plot in Python using Matplotlib

A Tri-Surface Plot is a type of surface plot, created by triangulation of compact surfaces of finite number of triangles which cover the whole surface in a manner that each and every point on the surface is in triangle. The intersection of any two triangles results in void or a common edge or vertex. This type of plot is created where the evenly sampled grids are restrictive and inconvenient to plot. Generally Tri-Surface plots are created by calling ax.plot_trisurf() function of matplotlib library.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

z1 = np.linspace(0, 5000, 100)
x1 = np.sin(z1)
y1 = np.cos(z1)

fig1 = plt.figure(figsize=(12, 7))
axis1 = fig1.add_subplot(111, projection='3d')

axis1.plot_surface(x1, y1, z1[:, np.newaxis], linewidth=0.4, antialiased=True)

plt.show()





# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# Creating dataset
z = np.linspace(0, 50000, 100)
x = np.sin(z)
y = np.cos(z)

# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

# Creating plot
ax.plot_trisurf(x, y, z,
				linewidth = 0.2,
				antialiased = True);

# show plot
plt.show()





"""
For better understanding Let’s take another example. 
"""

r2 = np.linspace(0.125,1.0,100)
a2 = np.linspace(0,2*np.pi,100,endpoint=False)
a2 = np.repeat(a2[...,np.newaxis],100,axis=1)
x2 = np.append(0,(r2*np.cos(a2)))
y2 = np.append(0,(r2*np.sin(a2)))
z2 = (np.sin(x2**4)+np.cos(y2**4))

fig2 = plt.figure(figsize=(14,8))
axis2 = plt.axes(projection='3d')

cmap2 = plt.get_cmap('cool')
tri_surf2 = axis2.plot_trisurf(x2,y2,z2,
                               cmap=cmap2,
                               linewidth=.2,
                               antialiased=True,
                               edgecolor='gold',
                               )
fig2.colorbar(tri_surf2,ax=axis2,shrink=.5,aspect=5)
axis2.set_title("Tri surface plotting np.sin and np.cos")

axis2.set_xlabel('X-axis')
axis2.set_ylabel('Y-axis')
axis2.set_zlabel('Z-axis')
plt.show()


"""
Surface plots and Contour plots in Python

Matplotlib was introduced keeping in mind, only two-dimensional plotting. But at the time when the release of 1.0 occurred, the 3d utilities were developed upon the 2d and thus, we have 3d implementation of data available today! The 3d plots are enabled by importing the mplot3d toolkit. In this article, we will discuss the surface plots and contour plots in detail.

Surface plots
A Surface Plot is a representation of a three-dimensional dataset. It describes a functional relationship between two independent variables X and Z and a designated dependent variable Y, rather than showing the individual data points. It is a companion plot of the contour plot. It is similar to the wireframe plot, but each face of the wireframe is a filled polygon. This helps to create the topology of the surface which is being visualized.

Surface plots are used to :

Visualise loss functions in machine learning and deep learning
Visualise store or state value functions in reinforcement learning
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a3 = np.array([1, 2, 3])
b3 = np.array([4, 5, 6, 7])

a3, b3 = np.meshgrid(a3, b3)

# surface plot for a + b
fig3 = plt.figure()
axes = fig3.add_subplot(111, projection='3d')
axes.plot_surface(a3, b3, a3 + b3)

plt.show()

print("-------------------------------------")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

a, b = np.meshgrid(a, b)

# surface plot for a**2 + b**2
a = np.arange(-1, 1, 0.02)
b = a
a, b = np.meshgrid(a, b)

fig = plt.figure()
axes = fig.add_subplot(111,projection ='3d')
axes.plot_surface(a, b, a**2 + b**2,cmap='viridis')

plt.show()
"""
Creating Contour plots
The matplotlib.pyplot.contour() are usually useful when Z = f(X, Y) i.e Z changes as a function of input X and Y. A contourf() is also available which allows us to draw filled contours.

Syntax:

matplotlib.pyplot.contour([X, Y, ] Z, [levels], **kwargs)
where,

X, Y: 2-D NumPy arrays with the same shape as Z or 1-D arrays such that len(X)==M and len(Y)==N (where M and N are rows and columns of Z)
Z: The height values over which the contour is drawn. The shape is (M, N)
levels: Determines the number and positions of the contour lines/regions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

a, b = np.meshgrid(a, b)

# surface plot for a**2 + b**2
a = np.arange(-1, 1, 0.02)
b = a
a, b = np.meshgrid(a, b)

fig = plt.figure()
axes = fig.add_subplot(111,projection ='3d')
axes.contour(a, b, a**2 + b**2,cmap='viridis')

plt.show()


"""
How to change angle of 3D plot in Python?

Prerequisites: Matplotlib, NumPy

In this article, we will see how can we can view our graph from different angles, Here we use three different methods to plot our graph. Before starting let’s see some basic concepts of the required module for this objective.

Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack
Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python
mpl_toolkits provides some basic 3D plotting (scatter, surf, line, mesh) tools.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#plt.figure - plots the view area as per the size we provide
fig4 = plt.figure(figsize=(10,7))
#plt.axes for projecting the graph as per the axis wise and projection='3d' for projecting into 3d
axis4 = plt.axes(projection='3d')

#np.linspace - initial point, final point , value to be taken from the range
z4 = np.linspace(0,100,100)
#np.sin - sin function for z4 
x4 = np.sin(z4)
#np.cos - cos function for z4
y4 = np.cos(z4)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#for some axis plot3D plots the graph as per the x,y,z values
axis4.plot3D(x4,y4,z4)
#for the working axis view_init - the starting angle and ending angle for the area
axis4.view_init(60,40)
plt.show()

print("-------------------------------------------")



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#plt.figure - plots the view area as per the size we provide
fig4 = plt.figure(figsize=(8,8))
#plt.axes for projecting the graph as per the axis wise and projection='3d' for projecting into 3d
axis4 = plt.axes(projection='3d')

#np.linspace - initial point, final point , value to be taken from the range
z4 = np.linspace(0,15,1000)
#np.sin - sin function for z4 
x4 = np.sin(z4)
#np.cos - cos function for z4
y4 = np.cos(z4)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#for some axis plot3D plots the graph as per the x,y,z values
axis4.plot3D(x4,y4,z4)

axis4.set_zlabel("Z-axis")
#for the working axis view_init - the starting angle and ending angle for the area
axis4.view_init(30,150)
plt.show()

"""
plotting the rectangular plate 
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
#declaring the size of graph
fig5 = plt.figure(figsize=(10,7))
#plotting the graph
axis5 = fig5.add_subplot(111,projection='3d')

#dataset limit 
x5 = np.linspace(-1,1,100)
y5 = np.linspace(-1,1,100)
x5,y5 = np.meshgrid(x5,y5)

#dataset for z index
z5 = x5+y5
#a5 is the rotating angle
a5 = int(input("Enter the rotating angle: "))

#trasnpose of the give array
t5 = np.transpose(np.array([x5,y5,z5]),(1,2,0))

#plotting the matrices in 3x3 for 3d plotting
m5 = [[np.cos(a5),0,np.sin(a5)],[0,1,0],
      [-np.sin(a5),0,np.cos(a5)]
      ]
#dot product
X,Y,Z = np.transpose(np.dot(t5,m5),(2,0,1))
axis5.plot_surface(X,Y,Z,alpha=.5)
plt.show()


"""
How to animate 3D Graph using Matplotlib?

Prerequisites: Matplotlib, NumPy

Graphical representations are always easy to understand and are adopted and preferable before any written or verbal communication. With Matplotlib we can draw different types of Graphical data. In this article, we will try to understand, How can we create a beautiful graph using matplotlib and create a 3D animated Graph using Matplotlib.

Approach:

Import required module.
Create a 3d figure
Create sample data
Animate 360 views of the graph.
Display Graph.
"""

#import the necessary modules
import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal


fig6 = plt.figure(figsize=(10,8))
axis6 = plt.axes(projection='3d')

#dataset
data6 = np.linspace(0,1,1000,endpoint=True)

#plotting
axis6.plot3D(data6,signal.square(2*np.pi*5*data6))

#rotating with the angle
for angle in range(0,360):
    axis6.view_init(angle,30)
    plt.draw()
    plt.pause(.001)

plt.show()


# plot a spiral graph


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal
 
# Creating 3D figure
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')
 
# Creating Dataset
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'green')
 
# 360 Degree view
for angle in range(0, 360):
    ax.view_init(angle, 30)
    plt.draw()
    plt.pause(.001)
 
plt.show()