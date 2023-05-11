"""
---------------Basic operations---------------
Plethora of built-in arithmetic functions are provided in NumPy.

Operations on single array: We can use overloaded arithmetic operators to do element-wise operation on array to create a new array. In case of +=, -=, *= operators, the exsisting array is modified.
"""

import numpy as np
print("------------------arithmetic operations -- start  -----------------------------")
arr1 = np.array([4,5,6,8])
print("------------------actual value in matrices-----------------------------")
print("Actual values:",arr1)

#adding some values to each elements in matrices
#Note: only the addition can be done if theres 1 row only

print("---------------Adding some values to each elements-------------------------")
print("adding value to each elements",arr1+1)

print("----------------getting powered value for each element----------------------")
print("exponentation:",arr1**int(input("Enter power values: ")))

print("------------------arithmetic operations -- end -----------------------------")


print("------------------unary operations -- start  -----------------------------")

arr2 = np.array([[5,5,6],
         [7,9,3],
         [8,4,2]
         ])
print("---------------getting max value-------------------------")
print(arr2.max())
print("Row wise",arr2.max(axis=1))

print("---------------getting min value-------------------------")
print(arr2.min())

print("sum of array elemenst:",arr2.sum())

print("------------------unary operations -- ends -----------------------------")

print("------------------binary operations -- start  -----------------------------")


arr3 = np.array([[5,5,6],
[7,9,3],
[8,4,2]
])
arr4=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("------------------adding two matrices-----------------------------")
print(arr3+arr4)
print("------------------getting dot product of two matrices -----------------------------")
print(arr3.dot(arr4))
print("------------------binary operations -- ends -----------------------------")
print("------------------universal functions -- start  ---------------------------")
arr5 = np.array([np.pi/3,np.pi/4,np.pi])
print("Sin value: ",np.sin(arr5))
print("Cos value: ",np.cos(arr5))
print("Tan value: ",np.tan(arr5))
print("-----------------universal operations -- ends  -----------------------------")
