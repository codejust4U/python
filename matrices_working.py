import numpy as np
matrix1 = np.array([
[1,1,1,1],
[1,2,3,4],
[4,5,8,2]
])

matrix2 = np.transpose(matrix1)

mul_matrix1 = np.matmul(matrix1,matrix2)
print(mul_matrix1)

print(np.linalg.inv(mul_matrix1))