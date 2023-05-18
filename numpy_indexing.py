"""
----------------------Numpy | Indexing-----------------------
NumPy or Numeric Python is a package for computation on homogenous n-dimensional arrays. In numpy dimensions are called as axes.

--------------------Why do we need NumPy ?--------------------

A question arises that why do we need NumPy when python lists are already there. The answer to it is we cannot perform operations on all the elements of two list directly. For example, we cannot multiply two lists directly we will have to do it element-wise. This is where the role of NumPy comes into play.
"""

list1 = [2,4,6,7,8]
list2 = [3,5,7,9,10]
print("------------------------------------------------------------------------------")
#mulitplying twi lists directly which will generate the error as --------------- TypeError: can't multiply sequence by non-int of type 'list'

#print(list1*list2)
print("------------------------Multiple of two list with the help of Numpy-----------------------")
import numpy as np

l1 = np.array(list1)
l2 = np.array(list2)

#now we are multiplying the two lists with the help of numpy
print(l1*l2)
print("------------------------------------------------------------------------------")

a = np.arange(10, 1, -3) 
print("\n A sequential array with a negative step: \n",a)
 
# Indexes are specified inside the np.array method.
newarr = a[np.array([1, 1, 2 ])]
print("\n Elements at these indices are:\n",newarr)
print("------------------------------------------------------------------------------")

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
 
# Index values can be negative.
arr = x[np.array([1, 3, -3])]
print("\n Elements are : \n",arr)
print("------------------------------------------------------------------------------")
