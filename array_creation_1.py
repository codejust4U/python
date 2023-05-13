"""
----------------Numpy | Array Creation---------------------

Array creation using List : Arrays are used to store multiple values in one single variable.Python does not have built-in support for Arrays, but Python lists can be used instead.
"""
print("----------------Numpy | Array Creation using list---------------------")
normal_arr = [1,2,3,4]
for i in normal_arr:
    print(i)

print("----------------------------------------------------------------------------")

"""
------------------Array creation using array functions :----------------------
array(data type, value list) function is used to create an array with data type and value list specified in its arguments.
"""
import array
through_array = array.array('i',[98,34,67,21])
print("through array ")
for i in range(len(through_array)):
    print(through_array[i],end=" ")

print("\n----------------------------------------------------------------------------")

"""
----------------------Array creation using numpy methods :-------------------------
NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation. For example: np.zeros,np.empty etc.

numpy.empty(shape, dtype = float, order = ‘C’) : Return a new array of given shape and type, with random values.
"""

import numpy as np

print("Creating empty or zeros array")

a = np.empty([2, 2], dtype = int)
print("\nMatrix a : \n", a)
print("Note that the specific values will be different each time you run the code because the array is not initialized and contains whatever random values were in memory at the time of allocation.")

b = np.zeros([3,3 ], dtype = int)
print("\n",b)
print("----------------------------------------------------------------------------")

"""
Reshaping array: We can use reshape method to reshape an array. Consider an array with shape (a1, a2, a3, …, aN). We can reshape and convert it into another array with shape (b1, b2, b3, …, bM).
The only required condition is: a1 x a2 x a3 … x aN = b1 x b2 x b3 … x bM . (i.e original size of array remains unchanged.)

numpy.reshape(array, shape, order = ‘C’) : Shapes an array without changing data of array.
"""

arr = np.arange(9)
print("The array before its reshaped: ",arr)

arr = np.arange(9).reshape(3,3)
print("\nThe array after reshaping: \n",arr)
print("----------------------------------------------------------------------------")
arr = np.arange(8)
print("The array before its reshaped: ",arr)
arr = np.arange(8).reshape(2,2,2)
print("\nThe array after reshaping: \n",arr)
print("----------------------------------------------------------------------------")

"""
To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
arange returns evenly spaced values within a given interval. step size is specified.
linspace returns evenly spaced values within a given interval. num no. of elements are returned.

arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. The interval mentioned is half opened i.e. [Start, Stop)
"""
print("The array with range values: \n",np.arange(4,10))

print("----------------------------------------------------------------------------")

"""
numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None) : Returns number spaces evenly w.r.t interval. Similiar to arange but instead of step it uses sample number.
"""

print("Number of elements with some gaps: \n",np.linspace(2.0,3.0,num=10))

sin_arr = np.linspace(0,2,10)
print("\nTo evaluate sin() in long range \n",np.sin(sin_arr))
