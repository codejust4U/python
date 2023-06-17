"""
Working with Images in Python using Matplotlib

Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack.

Working with Images in Python using Matplotlib
The image module in matplotlib library is used for working with images in Python. The image module also includes two useful methods which are imread which is used to read images and imshow which is used to display the image.
"""

import matplotlib.pyplot as plt
import matplotlib.image as img

t_image1 = img.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\image1.png')
plt.imshow(t_image1)

"""
The below program reads an image and then represents the image in array.
"""

import matplotlib.pyplot as plt
import matplotlib.image as img

t_image1 = img.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\image1.png')
print(t_image1)

"""
Here, the shape of the image is (225, 225, 3) which represents (height, width, mode) of the image, for colored image mode value is from 0 to 2 and for black and white image mode value is 0 and 1 only. In the output image, only the mode of the image is modified.
"""

import matplotlib.pyplot as plt
import matplotlib.image as img

#getting the image as source
t_image1 = img.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\image1.png')
#shape of image
print(t_image1.shape)

#modifying the image
mdfd_img = t_image1[:, :, 0]    #if last will be : then it goes back to original 

plt.imshow(mdfd_img)


"""
Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was introduced by John Hunter in the year 2002.
One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data in easily digestible visuals. Matplotlib consists of several plots like line, bar, scatter, histogram etc.

"""

# reading png image file
t_image2 = img.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\bnw.png')
  
# show image
plt.imshow(t_image2)

"""
 # Applying pseudocolor to image

Pseudocolor is useful for enhancing contrast of image.
"""

# reading png image file
t_image2 = img.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\bnw.png')

#adding luminosity to image
lum_img = t_image2[:, :, 0]

# show image
plt.imshow(lum_img)



# reading png image file
t_image3 = img.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\bnw.png')

#adding luminosity to image
lum_img3 = t_image3[:, :, 0]

# show image
plt.imshow(lum_img3,cmap='hot')
plt.colorbar()


"""
Interpolation Schemes:
Interpolation calculates what the color or value of a pixel “should” be and this needed when we resize the image but want the same information. There’s missing space when you resize image because pixels are discrete and interpolation is how you fill that space.
"""


from PIL import Image 
import matplotlib.pyplot as plt
  
# reading png image  file
img5 = Image.open(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\bnw.png')
  
# resizing the image
img5.thumbnail((50, 50), Image.ANTIALIAS)
imgplot = plt.imshow(img5)


"""
# ‘bicubic’ value is used for interpolation.
"""

import matplotlib.pyplot as plt
  
# importing image from PIL
from PIL import Image 
  
# reading image
img6 = Image.open(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\bnw.png')
  
img6.thumbnail((30, 30), Image.ANTIALIAS) 
  
# bicubic used for interpolation
imgplot = plt.imshow(img6, interpolation ='bicubic')


"""
# ‘sinc’ value is used for interpolation.
"""

from PIL import Image 
import matplotlib.pyplot as plt
  
# reading image
img7 = Image.open(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\bnw.png')
  
img7.thumbnail((30, 30), Image.ANTIALIAS)
  
# sinc used for interpolation
imgplot = plt.imshow(img7, interpolation ='sinc')



"""
Syntax: matplotlib.pyplot.imshow(X, cmap=None)

Displaying Grayscale image
Displaying Grayscale image, store the image path here let’s say it fname. Now open the image using PIL image method and convert it to L mode If you have an L mode image, that means it is a single-channel image – normally interpreted as grayscale. It only stores a grayscale, not color. Plotting the image as cmap = ‘gray’ converts the colors. All the work is done you can now see your image.
"""

#fetching the image
f_img8 = r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\texted.png'
#image opened with PIL
img8 = Image.open(f_img8).convert("L")

#plotting with cmap
plt.imshow(img8, cmap='gray')
plt.show()


"""

Matplotlib and its constituents support a lot of functionality. One such functionality is that we can draw a line or a point on an image using Matplotlib in python.

Approach
Import modules
Read the image
Plot the line or point on the image
Display the plot/image.
"""


from matplotlib import image
from matplotlib import pyplot as plt
  
# to read the image stored in the working directory
data10 = image.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\beach.png')

x10_1 = [100,500]
y10_1 = [400,100]
x10_2 = [150,450]
y10_2 = [100,400]

# to draw a point on co-ordinate (200,300)
plt.plot(x10_1,y10_1,x10_2,y10_2, color="white",linewidth=3)
plt.axis('off')
plt.imshow(data10)
plt.show()


"""
Syntax: Rectangle(xy, width, height, angle=0.0, **kwargs)

Parameters:

xy: Lower left point to start the rectangle plotting
width : width of the rectangle
height: Height of the rectangle.
angle: Angle of rotation of the rectangle.
Approach
Import the necessary libraries. 
Insert and display the image.
Create the figure and axes of the plot 
Add the patch to the Axes
Display the image
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as img
import matplotlib.patches as pt

#fetching the image
d_img11 = np.array(img.open(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\texted.png'),dtype=np.uint8)
plt.imshow(d_img11)

#creating figure and axis
fig11,axis11 = plt.subplots(1)
#disply axis
axis11.imshow(d_img11)

#making rectangle
r_img11 = pt.Rectangle((250,100),40,30, linewidth=1,edgecolor='r',facecolor='gold')

#adding patch to axis
axis11.add_patch(r_img11)
plt.show()

"""
The OpenCV module is an open-source computer vision and machine learning software library. It is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. When it is integrated with various libraries, such as numpy which is a highly optimized library for numerical operations, then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.

First, let’s look at how to display images using OpenCV:

Now there is one function called cv2.imread() which will take the path of an image as an argument. Using this function you will read that particular image and simply display it using the cv2.imshow() function. 


"""

import cv2

# Fetching the image
image13 = cv2.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\texted.png')

# Display
cv2.imshow("Image", image13)
cv2.waitKey(0)
