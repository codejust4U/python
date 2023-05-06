"""
---------------N-Dimensional array(ndarray) in Numpy---------------
Array in Numpy is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In Numpy, number of dimensions of the array is called rank of the array.A tuple of integers giving the size of the array along each dimension is known as shape of the array. An array class in Numpy is called as ndarray. Elements in Numpy arrays are accessed by using square brackets and can be initialized by using nested Python Lists.
"""

# importing numpy
import numpy as np

array1 = np.array([[1, 2, 3],
                   [4, 2, 5]])
# implementing some functions on numpy
# for getting the array type
print("Type of array is: ", type(array1))

# for getting the length of array
print("Length of array: ", len(array1))

# getting the dimensions of array or rank
print(array1.ndim)

# getting the size of array
print(array1.size)

# getting the shape of array
print(array1.shape)

# for getting thr datatype of each element
print("Array store element of array: ", array1.dtype)


arr1 = np.array([[1, 2, 3], [4, 5, 6]], dtype='float')
# for creating an array with passed list
print("Through passed list: \n", arr1)
print("\n")

# creatint the array with tuples
arr2 = np.array((1, 4, 7))
print("Through tuple : \n", arr2)
print("\n")

# creating the array with zeros
arr3 = np.zeros((3, 4))
print("Zeros array : \n", arr3)
print("\n")

# for creating the complex array
arr4 = np.full((3, 3), 6, dtype='complex')
print("Complex array with 6 real: \n", arr4)
