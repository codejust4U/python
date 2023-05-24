import numpy as np
"""
Sorting
Sorting refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a particular order. Most common orders are in numerical or lexicographical order. In Numpy, we can perform various sorting operations using the various functions that are provided in the library like sort, lexsort, argsort etc.

numpy.sort() : This function returns a sorted copy of an array.
"""
print("---------------------------Sorting - Numpy----------------------------------")
print("---------------------------Sorting along axis 0 -----------------------------")
array1 = np.array([[10,45],[23,98]])
sorted_array1 =np.sort(array1,axis=0)
print(sorted_array1)
print("-----------------------------------------------------------------------------")
print("---------------------------Sorting along axis -1 ----------------------------")
array2 = np.array([[10,45],[23,98]])
sorted_array2 =np.sort(array2,axis=-1)
print(sorted_array2)
print("-----------------------------------------------------------------------------")
print("---------------------------Sorting along no axis ----------------------------")
array3 = np.array([[10,45],[23,98]])
sorted_array3 =np.sort(array3,axis=None)
print(sorted_array3)
print("-----------------------------------------------------------------------------")

"""
numpy.argsort() : This function returns the indices that would sort an array.
"""
print("-------------------------------arg sort()--------------------------------")
print("-------------------------------Unsorted array--------------------------------")
array4 = np.array([3,4,8,2,1,0,3,4,5])
print(array4)
print("--------------------------------Half sorted----------------------------------")
sorted_array4 = np.argsort(array4)
print(sorted_array4)
print("-----------------------------complete sorted---------------------------------")
complete_sorted_array4 = np.zeros(len(sorted_array4),dtype=int)
for i in range(0,len(sorted_array4)):
    complete_sorted_array4[i] = array4[sorted_array4[i]]
print(complete_sorted_array4)
print("-----------------------------------------------------------------------------")

"""
numpy.lexsort() : This function returns an indirect stable sort using a sequence of keys.
"""
print("-------------------------------lex sort()--------------------------------")
array5 = np.array([3,4,8,2,1,0,3,4,5])
array6 = np.array([4,7,2,0,3,5,3,2,9])
for (i,j) in zip(array5,array6):
    print(i,' ',j)

sorted_array5_6 = np.lexsort((array6,array5))
print(sorted_array5_6)
print("-----------------------------------------------------------------------------")

"""
FUNCTION	                            DESCRIPTION
numpy.ndarray.sort()	        Sort an array, in-place.
numpy.msort()	                       Return a copy of an array sorted along the first axis.
numpy.sort_complex()	            Sort a complex array using the real part first, then the imaginary part.
numpy.partition()	                    Return a partitioned copy of an array.
numpy.argpartition()	              Perform an indirect partition along the given axis using the algorithm specified by the kind keyword.

"""

"""
Searching
Searching is an operation or a technique that helps finds the place of a given element or value in the list. Any search is said to be successful or unsuccessful depending upon whether the element that is being searched is found or not. In Numpy, we can perform various searching operations using the various functions that are provided in the library like argmax, argmin, nanaargmax etc.

numpy.argmax() : This function returns indices of the max element of the array in a particular axis.
"""
print("---------------------------Searching - Numpy----------------------------------")
matrix1 = np.arange(15).reshape(5,3)
print(matrix1)
print("-------------------------------Max element------------------------------------")
max_elmt = np.argmax((matrix1))
print(max_elmt)
print("-----------------------------Amx element asix - 0 ----------------------------")
print((np.argmax(matrix1,axis=0)))
print("-----------------------------Amx element asix - 1 ----------------------------")
print((np.argmax(matrix1,axis=1)))
print("-----------------------------------------------------------------------------")

"""
Counting
numpy.count_nonzero() : Counts the number of non-zero values in the array .
"""

print("---------------------------Counting- Numpy----------------------------------")
print("-------------------------Counting nonzero without axis------------------------")
non_zeros1 = np.count_nonzero([[2, 6, 3, 5], [3, 2, 6, 0]])
print(non_zeros1)
print("-------------------------Counting nonzero with axis------------------------")
non_zeros2 = np.count_nonzero([[2, 6, 3, 5], [3, 2, 6, 0]], axis=0)
print(non_zeros2)
