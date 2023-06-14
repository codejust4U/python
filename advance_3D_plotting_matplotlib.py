"""
3D Scatter Plotting in Python using Matplotlib

A 3D Scatter Plot is a mathematical diagram, the most basic version of three-dimensional plotting used to display the properties of data as three variables of a dataset using the cartesian coordinates.To create a 3D Scatter plot, Matplotlib’s mplot3d toolkit is used to enable three dimensional plotting.Generally 3D scatter plot is created by using ax.scatter3D() the function of the matplotlib library which accepts a data sets of X, Y and Z to create the plot while the rest of the attributes of the function are the same as that of two dimensional scatter plot.
Example 1: Let’s create a basic 3D scatter plot using the ax.scatter3D() function.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

z1 = np.random.randint(100,size=(50))
x1 = np.random.randint(80,size=(50))
y1 = np.random.randint(60,size=(50))

fig1 = plt.figure(figsize=(8,6))
axis1 = plt.axes(projection='3d')
#cmap1 = plt.get_cmap('hsv')
axis1.scatter3D(x1,y1,z1)
#axis1.scatter3D(y1,color='gold')
#axis1.scatter3D(z1,color='blue')
plt.title("3D scatter plotting")

plt.show()

"""
Each axis scattered with each color
"""

z2 = 4 * np.tan(np.random.randint(10,size=(200)))+np.random.randint(100,size=(200))
x2 = 4*np.cos(z2)+np.random.normal(size=200)
y2 = 4*np.sin(z2)+4*np.random.normal(size=200)

fig2 = plt.figure(figsize=(16,9))
axis2 = plt.axes(projection='3d')
axis2.grid(b=True, color='gold',
           linestyle='-.',linewidth=.3,
           alpha=.7)

cmap2 = plt.get_cmap('hsv')
scatter2 = axis2.scatter3D(x2,y2,z2,
                           alpha=.8,
                           c = (x2+y2+z2),
                           cmap = cmap2,
                           marker = '*'
                           )
plt.title('3D plot - each axis with different color')
axis2.set_xlabel("X-axis")
axis2.set_ylabel("Y-axis")
axis2.set_zlabel("Z-axis")

fig2.colorbar(scatter2, ax=axis2, shrink=.5,
              aspect=5)

plt.show()

"""
3D Surface plotting in Python using Matplotlib

A Surface Plot is a representation of three-dimensional dataset. It describes a functional relationship between two independent variables X and Z and a designated dependent variable Y, rather than showing the individual data points. It is a companion plot of the contour plot. It is similar to the wireframe plot, but each face of the wireframe is a filled polygon. This helps to create the topology of the surface which is being visualized.
 

Creating 3D surface Plot
The axes3d present in Matplotlib’s mpl_toolkits.mplot3d toolkit provides the necessary functions used to create 3D surface plots.Surface plots are created by using ax.plot_surface() function.
Syntax: 

ax.plot_surface(X, Y, Z)
where X and Y are 2D array of points of x and y while Z is 2D array of heights.
"""
x3 = np.outer(np.linspace(-3,3,32),np.ones(32))
y3 = x3.copy().T
z3 = (np.sin(x3**2)+np.cos(y3**2))
fig3 = plt.figure(figsize=(16,9))
axis3 = plt.axes(projection='3d')
axis3.plot_surface(x3,y3,z3,edgecolor='gold',cmap='cool',alpha=.5)
plt.show()


"""
Gradient surface Plot
Gradient surface plot is a combination of 3D surface plot with a 2D contour plot. In this plot the 3D surface is colored like 2D contour plot. The parts which are high on the surface contains different color than the parts which are low at the surface.
Syntax:

surf = ax.plot_surface(X, Y, Z, cmap=, linewidth=0, antialiased=False)

The attribute cmap= sets the color of the surface. A color bar can also be added by calling fig.colorbar. 
"""
x4 = np.outer(np.linspace(-3,3,32),np.ones(32))
y4 = x4.copy().T
z4 = (np.cos(x4**2)+np.sin(y4**2))
fig4 = plt.figure(figsize=(16,9))
axis4 = plt.axes(projection='3d')

cmap4 = plt.get_cmap('hot')
surf4 = axis4.plot_surface(x4,y4,z4,
                           cmap=cmap4,
                           edgecolor='none')
fig4.colorbar(surf4,ax=axis4,
              shrink=.5,
              aspect=5)
axis4.set_title("Surface plot")
plt.show()

"""
3D surface Plot having 2D contour plot projections
3D surface plots plotted with Matplotlib can be projected on 2D surfaces. The code below creates a 3D plots and visualizes its projection on 2D contour plot:
"""

x5 = np.outer(np.linspace(-3,3,32),np.ones(32))
y5 = x5.copy().T
z5 = (np.sin(x5**2)+np.cos(y5**2))
fig5 = plt.figure(figsize=(16,9))
axis5 = plt.axes(projection='3d')

cmap5 = plt.get_cmap('cool')  #cmap = hot
surf5 = axis5.plot_surface(x5,y5,z5,
                           rstride=8,
                           cstride=8,
                           alpha=.6,
                           cmap=cmap5)
cset5 = axis5.contour(x5,y5,z5,
                      zdir='z5',
                      offset=np.min(z5),
                      cmap=cmap5)
cset5 = axis5.contour(x5,y5,z5,
                      zdir='x5',
                      offset=-5,
                      cmap=cmap5)
cset5 = axis5.contour(x5,y5,z5,
                      zdir='y5',
                      offset=5,
                      cmap=cmap5)
fig5.colorbar(surf5,ax=axis5,shrink=.5,aspect=5)
axis5.set_xlabel('X-axis')
axis5.set_xlim(-5,5)
axis5.set_ylabel('Y-axis')
axis5.set_ylim(-5,5)
axis5.set_zlabel('Z-axis')
axis5.set_zlim(np.min(z5),np.max(z5))

axis5.set_title("3D surface plot wiht contour projection")

plt.show()

"""
Trignometric wireframe plotting
"""


a7 = np.linspace(-5,5,25)
b7 = np.linspace(-5,5,25)
x7,y7 = np.meshgrid(a7,b7)
z7 = np.sin(np.sqrt(x7**2+y7**2))
fig7 = plt.figure()
wf7 = plt.axes(projection='3d')
wf7.plot_wireframe(x7,y7,z7,color='gold')
wf7.set_title("Trignometric Sin 3D wireframe plot")
plt.show()





a7 = np.linspace(-5,5,25)
b7 = np.linspace(-5,5,25)
x7,y7 = np.meshgrid(a7,b7)
z7 = np.cos(np.sqrt(x7**2+y7**2))
fig7 = plt.figure()
wf7 = plt.axes(projection='3d')
wf7.plot_wireframe(x7,y7,z7,color='red')
wf7.set_title("Trignometric Cos 3D wireframe plot")
plt.show()



"""
3D Contour Plotting in Python using Matplotlib

Matplotlib was introduced keeping in mind, only two-dimensional plotting. But at the time when the release of 1.0 occurred, the 3d utilities were developed upon the 2d and thus, we have 3d implementation of data available today! The 3d plots are enabled by importing the mplot3d toolkit. Let’s look at a 3d contour diagram of a 3d cosine function.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x8 = np.arange(0, 200, 100)
y8 = np.arange(0, 200, 100)
x8, y8 = np.meshgrid(x8, y8)
z8 = np.cos(np.sqrt(x8*2 + y8*2))

fig8 = plt.figure()
axis8 = fig8.add_subplot(111, projection='3d')
axis8.contour3D(x8, y8, z8, 50, cmap=cm.cool)
axis8.set_xlabel('A')
axis8.set_ylabel('B')
axis8.set_zlabel('C')
axis8.set_title('3D contour for Cos')
plt.show()



from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math

x = [i for i in range(0, 200, 100)]
y = [i for i in range(0, 200, 100)]

X, Y = np.meshgrid(x, y)
Z = []
for i in x:
	t = []
	for j in y:
		t.append(math.tan(math.sqrt(i*2+j*2)))
	Z.append(t)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap=cm.cool)
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_title('3D contour for tan')
plt.show()
