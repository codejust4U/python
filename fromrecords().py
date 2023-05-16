"""
---------------------Python | Numpy fromrecords() method---------------------
With the help of numpy.core.fromrecords() method, we can create the record array by using the list of individual records by using numpy.core.fromrecords() method.

Syntax : numpy.core.fromrecords([(tup1), (tup2)], metadata)

Return : Return the record of an array.
"""
print("------------------------------------------------------------------------------")
import numpy as np
print("---------------------------------Fromrecords() in numpy ---------------------------------------------")
fr = np.core.records.fromrecords([(50,'pankaj',22),
                                  (60,'sai',23),
                                  (70,'rai',24)],
                                 names = 'rollno,name,age')

print(fr[2])
print(fr.name)
print("------------------------------------------------------------------------------")
