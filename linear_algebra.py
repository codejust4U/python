"""
Numpy | Linear Algebra
The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.
One can find:

rank, determinant, trace, etc. of an array.
eigen values of matrices
matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
solve linear or tensor equations and much more!
"""

import numpy as np
matrix1 = np.array([
    [3,6,7],
    [9,2,5],
    [6,5,1]
])

print("--------------------------Linear Algebra - Numpy------------------------------")

print("--------------------------Rank of a matrix------------------------------")

rank = np.linalg.matrix_rank(matrix1)
print(rank)

print("------------------------------------------------------------------------------")
print("--------------------------Trace of a matrix------------------------------")
trace = np.trace(matrix1)
print(trace)
print("------------------------------------------------------------------------------")
print("--------------------------Determinant of a matrix-----------------------------")
determinant = np.linalg.det(matrix1)
print(determinant)
print("------------------------------------------------------------------------------")
print("--------------------------Inverse of a matrix-----------------------------")

inverse =np.linalg.inv(matrix1)
print(inverse)
print("------------------------------------------------------------------------------")
print("--------------------------Powered of a matrix-----------------------------")
#matrix_to_be_powered = int(input("Enter the number to get powered with it to the matrices value: "))
#powered_matrix = np.linalg.matrix_power(matrix1,matrix_to_be_powered)
powered_matrix = np.linalg.matrix_power(matrix1,2)
print(powered_matrix)
print("------------------------------------------------------------------------------")

"""
Matrix eigenvalues Functions
numpy.linalg.eigh(a, UPLO=’L’) : This function is used to return the eigenvalues and eigenvectors of a complex Hermitian (conjugate symmetric) or a real symmetric matrix.Returns two objects, a 1-D array containing the eigenvalues of a, and a 2-D square array or matrix (depending on the input type) of the corresponding eigenvectors (in columns).

numpy.linalg.eig(a) : This function is used to compute the eigenvalues and right eigenvectors of a square array.
"""
from numpy import linalg as np2
print("--------------------------Eigen matrix-----------------------------")
eign_matrix = np.array([[1, -2j], [2j, 5]])

print("Array is :", eign_matrix)


eign1,eign2 = np2.eigh(eign_matrix)

print("Eigen value is :", eign1)
print("Eigen value is :", eign2)

print("------------------------------------------------------------------------------")
print("--------------------------matrix and vector product---------------------------")
"""
Matrix and vector products
numpy.dot(vector_a, vector_b, out = None) : returns the dot product of vectors a and b. It can handle 2D arrays but considering them as matrix and will perform matrix multiplication. For N dimensions it is a sum product over the last axis of a and the second-to-last of b :

dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m]) 
"""
product  = np.dot(3,4)
print(product)
print("------------------------------------------------------------------------------")
"""
dot_product = vector1 * vector2
vector1 = 3 + 5j
vector2 = 2 + 3j

Using the formula for complex number multiplication:

dot_product = (3 + 5j) * (2 + 3j)

Expanding the expression:

dot_product = 3 * 2 + 3 * 3j + 5j * 2 + 5j * 3j
= 6 + 9j + 10j + 15j^2

Since j^2 is equal to -1:

dot_product = 6 + 9j + 10j - 15
= -9 + 19j

Therefore, the product of the given complex numbers is -9 + 19j.

"""
vector1 = 3 + 5j
vector2 = 2 + 3j
dot_product = np.dot(vector1,vector2)
print(dot_product)
print("------------------------------------------------------------------------------")
"""
numpy.vdot(vector_a, vector_b) : Returns the dot product of vectors a and b. If first argument is complex the complex conjugate of the first argument(this is where vdot() differs working of dot() method) is used for the calculation of the dot product. It can handle multi-dimensional arrays but working on it as a flattened array.
"""

vector_dot_product = np.vdot(vector1,vector2)
print(vector_dot_product)
print("------------------------------------------------------------------------------")
"""
Solving equations and inverting matrices
numpy.linalg.solve() : Solve a linear matrix equation, or system of linear scalar equations.Computes the “exact” solution, x, of the well-determined, i.e., full rank, linear matrix equation ax = b.
"""
print("-------------------Solving equations and inverting matrices--------------------")
matrix3 = np.array([
    [4,7],
    [7,1]
    ])

matrix4 = np.array([12,45])
linear_equations = np.linalg.solve(matrix3,matrix4)
print(linear_equations)
print("------------------------------------------------------------------------------")

"""
numpy.linalg.lstsq() : Return the least-squares solution to a linear matrix equation.Solves the equation a x = b by computing a vector x that minimizes the Euclidean 2-norm || b – a x ||^2. The equation may be under-, well-, or over- determined (i.e., the number of linearly independent rows of a can be less than, equal to, or greater than its number of linearly independent columns). If a is square and of full rank, then x (but for round-off error) is the “exact” solution of the equation.
"""

import matplotlib.pyplot as plt
 
side1 = np.arange(0,9)
array1 = np.array([side1, np.ones(9)])
# linearly generated sequence
sequence = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
prev_line = np.linalg.lstsq(array1.T, sequence)[0]
line = prev_line[0] * side1 + prev_line[1]  #regression line
plt.plot(side1, line,'r-')
plt.plot(side1, sequence, 'o')
plt.show()
