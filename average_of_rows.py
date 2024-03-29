"""
Data Science - Average of Rows


In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]
Explanation
The first row has two numbers 1.5 and 1, thus the sum is 1.5 + 1 = 2.5 and the mean is then 2.5/2 = 1.25. Then for the second row, the average is calculated as (2 + 2.9)/2 = 4.9/2 = 2.45.
"""


n, p = [int(x) for x in input().split()]
list = []
for i in range(n):
    list.append([float(j) for j in input().split()])
import numpy as np
arr = np.array(list, dtype='f')
mean = arr.mean(axis=1)
print(mean.round(2))
