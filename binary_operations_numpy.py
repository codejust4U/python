"""
Numpy | Binary Operations
Binary operators acts on bits and performs bit by bit operation. Binary operation is simply a rule for combining two values to create a new value.

numpy.bitwise_and() : This function is used to Compute the bit-wise AND of two array element-wise. This function computes the bit-wise AND of the underlying binary representation of the integers in the input arrays.
"""
print("------------------------------Binary Operations-------------------------------")
import numpy as np

input1  = int(input("Enter the number: "))
input2  = int(input("Enter the number: "))
print("--------------------------Binary Operations-  AND-----------------------------")
out_number = np.bitwise_and(input1,input2)
print("The bistwise AND of ",input1, "and ",input2,"is:",out_number)

print("------------------------------------------------------------------------------")

array1 = [8,4,67]
array2 = [4,9,23]

out_number2 = np.bitwise_and(array1,array2)
print("Bitwise AND of array1 and array2 : ",out_number2)
print("------------------------------------------------------------------------------")
print("--------------------------Binary Operations -  OR-----------------------------")
"""
numpy.bitwise_or() : This function is used to Compute the bit-wise OR of two array element-wise. This function computes the bit-wise OR of the underlying binary representation of the integers in the input arrays.
"""
out_number3 = np.bitwise_or(input1,input2)
print("The bistwise OR of ",input1, "and ",input2,"is:",out_number3)
print("------------------------------------------------------------------------------")
out_number4 = np.bitwise_or(array1,array2)
print("Bitwise OR of array1 and array2 : ",out_number4)


print("------------------------------------------------------------------------------")
print("--------------------------Binary Operations -  XOR----------------------------")
"""
numpy.bitwise_xor() : This function is used to Compute the bit-wise XOR of two array element-wise. This function computes the bit-wise XOR of the underlying binary representation of the integers in the input arrays.
"""
out_number5 = np.bitwise_xor(input1,input2)
print("The bistwise XOR of ",input1, "and ",input2,"is:",out_number5)
print("------------------------------------------------------------------------------")
out_number6 = np.bitwise_xor(array1,array2)
print("Bitwise XOR of array1 and array2 : ",out_number6)


print("------------------------------------------------------------------------------")
