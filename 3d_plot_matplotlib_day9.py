"""
Three-dimensional Plotting in Python using Matplotlib

3D plots are very important tools for visualizing data that have three dimensions such as data that have two dependent and one independent variable. By plotting data in 3d plots we can get a deeper understanding of data that have three variables. We can use various matplotlib library functions to plot 3D plots.

Example Of Three-dimensional Plotting using Matplotlib
We will first start with plotting the 3D axis using the Matplotlib library. For plotting the 3D axis we just have to change the projection parameter of plt.axes() from None to 3D.
"""
import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure()
axis1 = plt.axes(projection='3d')
"""
3-Dimensional Line Graph Using Matplotlib
For plotting the 3-Dimensional line graph we will use the mplot3d function from the mpl_toolkits library. For plotting lines in 3D we will have to initialize three variable points for the line equation. In our case, we will define three variables as x, y, and z
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig2 = plt.figure()
axis2 = plt.axes(projection='3d')

z = np.linspace(0,1,200)
x=z*np.sin(50*z)
y=z*np.cos(50*z)

axis2.plot3D(x,y,z,'lime',alpha=.5)
axis2.set_title("3D line plots")
plt.show()

"""
Dimensional Scattered Graph Using Matplotlib
To plot the same graph using scatter points we will use the scatter() function from matplotlib. It will plot the same line equation using distinct points. 
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig3 = plt.figure()
axis3 = plt.axes(projection='3d')

z = np.linspace(0,1,200)
x=z*np.sin(25*z)
y=z*np.cos(25*z)
c=x+y
axis3.scatter(x,y,z,c=c)
axis3.set_title("3D line plots with Scatter()")
plt.show()


"""
Surface Graphs using Matplotlib library  
Surface graphs and Wireframes graph work on gridded data. They take the grid value and plot it on a three-dimensional surface. We will use the plot_surface() function to plot the surface plot.
"""

x4 = np.outer(np.linspace(-2,2,10),np.ones(10))
y4 = x4.copy().T
z4 = np.cos(x4**2+y4**3)

fig4 = plt.figure()
axis4 = plt.axes(projection='3d')
axis4.plot_surface(x4,y4,z4,cmap='viridis',\
                   edgecolor='red')
axis4.set_title("3D plot with plot_surface()")
plt.show()

"""
Wireframes graph using Matplotlib library  
For plotting the wireframes graph we will use the plot_wireframe() function from the matplotlib library.
"""

def f(x5,y5):
    return np.sin(np.sqrt(x5**2+y5**2))

x5 = np.linspace(-1,5,10)
y5 = np.linspace(-1,5,10)

X5,Y5 = np.meshgrid(x5,y5)
Z5 = f(X5,Y5)

fig5 = plt.figure()
axis5 = plt.axes(projection='3d')
axis5.plot_wireframe(X5,Y5,Z5,color='lime')
axis5.set_title("3D plot with wireframe()")
plt.show()


"""
Contour Graphs using Matplotlib library
The contour graph takes all the input data in two-dimensional regular grids, and the Z data is evaluated at every point. We use the ax.contour3D function to plot a contour graph. Contour plots are an excellent way to visualize optimization plots. 
"""

def f6(x6,y6):
    return np.sin(np.sqrt(x6**2+y6**2))
x6 = np.linspace(-10,10,40)
y6 = np.linspace(-10,10,40)

X6,Y6 = np.meshgrid(x6,y6)
Z=f6(X6,Y6)

fig6 = plt.figure(figsize=(8,6))
axis6 = plt.axes(projection='3d')
axis6.plot_surface(X6,Y6,Z,cmap='cool',alpha=.5,edgecolor='gold')   #cmap='viridis' for yellow and green
axis6.set_title("3D counter plot function(x,y) \n sin(sqrt(x^2+y^2))",fontsize=14)
axis6.set_xlabel("X")
axis6.set_ylabel("Y")
axis6.set_zlabel("Z")
plt.show()


print("-------------------------------")


def f6(x6,y6):
    return np.cos(np.sqrt(x6**2+y6**2))
x6 = np.linspace(-10,10,40)
y6 = np.linspace(-10,10,40)

X6,Y6 = np.meshgrid(x6,y6)
Z=f6(X6,Y6)

fig6 = plt.figure(figsize=(8,6))
axis6 = plt.axes(projection='3d')
axis6.plot_surface(X6,Y6,Z,cmap='cool',alpha=.5,edgecolor='gold')   #cmap='viridis' for yellow and green
axis6.set_title("3D counter plot function(x,y) \n sin(sqrt(x^2+y^2))",fontsize=14)
axis6.set_xlabel("X")
axis6.set_ylabel("Y")
axis6.set_zlabel("Z")
plt.show()


"""
Plotting Möbius strip In Python 
Möbius strip also called the twisted cylinder, is a one-sided surface without boundaries. To create the Möbius strip think about its parameterization, it’s a two-dimensional strip, and we need two intrinsic dimensions. Its angle range from 0 to 2 pie around the loop and its width ranges from -1 to 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#parameters for Mobius strip
R7 = 2

u7 = np.linspace(0,2*np.pi, 100)
v7 = np.linspace(-1,1,100)
u7,v7 = np.meshgrid(u7,v7)
X7 = (R7+v7*np.cos(u7/2))*np.cos(u7)
Y7 = (R7+v7*np.cos(u7/2))*np.sin(u7)
z7 = v7*np.sin(u7/2)

fig7=plt.figure()
axis7 =  fig7.add_subplot(111,projection='3d',alpha=.9)

axis7.plot_surface(X7,Y7,z7)
axis7.set_xlabel('X')
axis7.set_ylabel('Y')
axis7.set_zlabel('Z')
axis7.set_title("Mobius Strip")

axis7.set_xlim([-3,3])
axis7.set_ylim([-3,3])
axis7.set_zlim([-3,3])

plt.show()