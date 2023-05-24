"""
numpy.linalg.lstsq() : Return the least-squares solution to a linear matrix equation.Solves the equation a x = b by computing a vector x that minimizes the Euclidean 2-norm || b – a x ||^2. The equation may be under-, well-, or over- determined (i.e., the number of linearly independent rows of a can be less than, equal to, or greater than its number of linearly independent columns). If a is square and of full rank, then x (but for round-off error) is the “exact” solution of the equation.
"""
print("--------------------------Use of pyplot--------------------------")
import numpy as np
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

print("-----------------------------------------------------------------------------")
