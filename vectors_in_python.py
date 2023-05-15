"""
Vector are built from components, which are ordinary numbers. We can think of a vector as a list of numbers, and vector algebra as operations performed on the numbers in the list. In other words vector is the numpy 1-D array.

Syntax : np.array(list)
Argument : It take 1-D list it can be 1 row and n columns or n rows and 1 column
Return : It returns vector which is numpy.ndarray

"""
import numpy as np
a = [1, 2, 3, 4, 5]
b = [[10],
     [20],
     [30],
     [40],
     [50]]

vector1 = np.array(a)
vector2 = np.array(b)

print("------------------------------Horizontal Vector-----------------------------")
print(vector1)

print("------------------------------------------------------------------------------")


print("--------------------------------Vertical Vector-----------------------------")
print(vector2)
print("------------------------------------------------------------------------------")

"""
Basic Arithmetic operation: 
In this example we will see do arithmetic operations which are element-wise between two vectors of equal length to result in a new vector with the same length 
"""
print("------------------------------Addition Vector-----------------------------")
addition = vector1+vector2
print(addition)
print("------------------------------------------------------------------------------")


print("------------------------------Subtraction Vector-----------------------------")
subtraction = vector1-vector2
print(subtraction)
print("------------------------------------------------------------------------------")


print("---------------------------Multiplication Vector-----------------------------")
multiplication = vector1*vector2
print(multiplication)
print("------------------------------------------------------------------------------")


print("---------------------------Division Vector-----------------------------")
division = vector1/vector2
print(division)
print("------------------------------------------------------------------------------")

"""
Vector Dot Product 
In mathematics, the dot product or scalar product is an algebraic operation that takes two equal-length sequences of numbers and returns a single number. 
For this we will use dot method.
"""

print("---------------------------Dot Product Vector-----------------------------")
dot_product = np.dot(vector1, vector2)
print(dot_product)
print("------------------------------------------------------------------------------")


"""
print("---------------------------Cross Product Vector-----------------------------")
cross_product = np.cross(vector1, vector2)
print(cross_product)
print("------------------------------------------------------------------------------")"""


vectors_ = np.array([11,22,33,44,55])
print("---------------------------vector - Vector-----------------------------")
print(vectors_)
print("------------------------------------------------------------------------------")
print("---------------------------vector - Scalar-----------------------------")
scalar = 2
print(scalar)
print("------------------------------------------------------------------------------")
"""
---------------------------Vector-Scalar Multiplication-----------------------------
Multiplying a vector by a scalar is called scalar multiplication. To perform scalar multiplication, we need to multiply the scalar by each component of the vector.
"""
print("---------------------------Scalar Multiplication-----------------------------")
scalar_multiplication = scalar*vectors_
print(scalar_multiplication)
print("------------------------------------------------------------------------------")
