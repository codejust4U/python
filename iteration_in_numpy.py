"""
Numpy | Iterating Over Array
NumPy package contains an iterator object numpy.nditer. It is an efficient multidimensional iterator object using which it is possible to iterate over an array. Each element of an array is visited using Python’s standard Iterator interface.
"""

import numpy as np

array1 = np.arange(25)
array1 = array1.reshape(5, 5)
print("-------------------------------original array--------------------------------")
print(array1)
"""
-------------Transposed array------------
The order of iteration is chosen to match the memory layout of an array, without considering a particular ordering. This can be seen by iterating over the transpose of the above array.
"""
print("--------------------------------Transposed array-------------------------------")

trans_array1 = array1.T
print(trans_array1)

print("-------------------------------Iterated array--------------------------------")
for i in np.nditer(array1):
    print(i)

print("-------------------------------------------------------------------------------")
print("-----------------------------C-style order----------------------------------")

for i1 in np.nditer(array1, order='C'):
  print(i1)

print("-------------------------------------------------------------------------------")
print("-----------------------------F-style order----------------------------------")
for i2 in np.nditer(array1, order='F'):
   print(i2)

print("-------------------------------------------------------------------------------")
print("-------------------Modification of Array Values---------------------")
print("Getting multiplication some number with the arrays values")
num = int(input("Enter the number: "))
for i3 in np.nditer(array1, op_flags=['readwrite']):
   i3 =  num * i3
   print(i3)
print("-------------------------------------------------------------------------------")

"""
External Loop:

The nditer class constructor has a flags parameter, which can take the following values

PARAMETER	DESCRIPTION
external_loop------Causes values given to be one-dimensional arrays with multiple values instead of zero-dimensional array
c_index	-----C_order index can be tracked
f_index	-----Fortran_order index is tracked
multi-index	------Type of indexes with one per iteration can be tracked

"""
print("-------------------C- index with external loop---------------------")

for i4 in np.nditer(array1,flags=['external_loop'], order='C'):
   print(i4)
print("-------------------------------------------------------------------------------")


print("-------------------F- index with external loop---------------------")
iteration = np.nditer(array1, flags=['f_index'])
while not iteration.finished:
   print("%d <%d>" %(iteration[0], iteration.index), end=" ")
   iteration.iternext()
print("\n------------------------------------------------------------------------------")
print("-------------------Broadcasting Iteration---------------------")
broadcasting_array = np.array([1], dtype=int)
print("To be Broadcasting Array: ",broadcasting_array)

for i5,i6 in np.nditer([array1,broadcasting_array]):
   print("%d:%d"% (i5,i6))

print("\n------------------------------------------------------------------------------")
