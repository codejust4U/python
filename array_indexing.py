"""
-----------Array Indexing-----------

Knowing the basics of array indexing is important for analysing and manipulating the array object. NumPy offers many ways to do array indexing.

Slicing: Just like lists in python, NumPy arrays can be sliced. As arrays can be multidimensional, you need to specify a slice for each dimension of the array.
Integer array indexing: In this method, lists are passed for indexing for each dimension. One to one mapping of corresponding elements is done to construct a new arbitrary array.
Boolean array indexing: This method is used when we want to pick elements from array which satisfy some condition."""

import numpy as np

# creating the array of 3x4
arr = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 0]
])

# Slicing array form 2 rows with alternate column 0 and 2
temp = arr[:2, ::2]
print("Slicing array form 2 rows with alternate column 0 and 2\n", temp)

# getting values through index- rows and column as(0,3),(0,2),(1,1),(2,0)
temp1 = arr[[0, 0, 1, 2], [3, 2, 1, 0]]
print("getting array value with rows and colums of (0,3),(0,2),(1,1),(2,0)\n", temp1, "\n")

greater_val = arr > 1
temp2 = arr[greater_val]
print("printing values greater than 1: ", temp2)
