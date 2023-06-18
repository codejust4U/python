"""
# How to Display an OpenCV image in Python with Matplotlib?

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

"""
Now let’s jump into displaying the images with Matplotlib module. It is an amazing visualization library in Python for 2D plots of arrays. The Matplotlib module is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack.
"""
import cv2
import matplotlib.pyplot as plt

#taking image as data
image1 = cv2.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\texted.png')

#calling imshow()
plt.imshow(image1)

#display the image
plt.show()

"""
# Making gray
"""

import cv2
import matplotlib.pyplot as plt

#taking image as data
image2 = cv2.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\texted.png')
#converting image into grayscale
image2_c = cv2.cvtColor(image2,cv2.COLOR_RGB2GRAY) 
#calling imshow()
plt.imshow(image2_c,cmap='gray')

#display the image
plt.show()


"""
Algorithm: 

Import the matplotlib.pyplot module.
Import an image using the imread() method.
Use the shape attribute of the image to get the height and width of the image. It fetches the number of channels in the image.
Calculate the area as, area = height * width.
Display the area.
"""

#importing modules
import matplotlib.pyplot as plt

image3 = cv2.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\texted.png')

#getting height and width
height3,width3, _ = image3.shape

#calculating area
area3 = height3*width3

#display area
print("Area of the image : ",area3)

print("--------------------------------")
#importing modules
import matplotlib.pyplot as plt

image4 = cv2.imread(r'C:\xampp\htdocs\practice\Python\python100dayscode\Day 97\beach.png')

#getting height and width
height4,width4, _ = image4.shape

#calculating area
area4 = height4*width4

#display area
print("Area of the image : ",area4)