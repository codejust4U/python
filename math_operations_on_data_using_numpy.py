"""
                                        Coder: Pankaj Kori
                                        Date: 04/30/2023

 ----------------Data Types in Numpy----------------
Every Numpy array is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. Every ndarray has an associated data type (dtype) object. This data type object (dtype) provides information about the layout of the array. The values of an ndarray are stored in a buffer which can be thought of as a contiguous block of memory bytes which can be interpreted by the dtype object. Numpy provides a large set of numeric datatypes that can be used to construct arrays. At the time of Array creation, Numpy tries to guess a datatype, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype.

----------------Constructing a Datatype Object----------------
In Numpy, datatypes of Arrays need not to be defined unless a specific datatype is required. Numpy tries to guess the datatype for Arrays which are not predefined in the constructor function.

 """

import numpy as np
import math
from decimal import getcontext, Decimal

x = np.array([1, 2])

print("Data Type: ", x.dtype)

float_type = np.array([2.0, 5.0])
print("Data Type: ", float_type.dtype)

string_type = np.array(["pk"])
print("Data Type: ", string_type.dtype)


"""
 ----------------Math Operations on DataType array----------------
 In Numpy arrays, basic mathematical operations are performed element-wise on the array. These operations are applied both as operator overloads and as functions. Many useful functions are provided in Numpy for performing computations on Arrays such as sum: for addition of Array elements, T: for Transpose of elements, etc.

"""
n = int(input("Enter the number of elements to be order of matrix: "))
a = []
b = []
c = []
d = []
print("enter the elements for 1st matrix: ")
for i in range(1, n):
    val_a = int(input())
    a.append(val_a)

for i in range(1, n):
    val_b = int(input())
    b.append(val_b)

print("enter the elements for 2nd matrix: ")
for i in range(1, n):
    val_c = int(input())
    c.append(val_c)

for i in range(1, n):
    val_d = int(input())
    d.append(val_d)


arr1 = np.array([a, b])
print(arr1)
print("\n")

arr2 = np.array([c, d])
print(arr2)
print("\n")

# Addition of two arrays
sum = np.add(arr1, arr2)
print("Addition of two arrays: \n", sum)
print("\n")

# Adding t he elements of arrays
add = np.sum(arr1)
print("Additon of elements: \n", add)
print("\n")

# Squaring each elements of matrix
square1 = np.sqrt(arr1)
result = np.round(square1, decimals=2)
print("Sqaure of matrix value: \n", result)
print("\n")

# Transpose of matrix
Transposed_arr = arr1.T
print("Transpose of 1st matrix: \n", Transposed_arr)
