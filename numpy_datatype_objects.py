"""
-------------------------Numpy | Data Type Objects-----------------------------
Every ndarray has an associated data type (dtype) object. This data type object (dtype) informs us about the layout of the array. This means it gives us information about :

Type of the data (integer, float, Python object etc.)
Size of the data (number of bytes)
Byte order of the data (little-endian or big-endian)
If the data type is a sub-array, what is its shape and data type.
The values of an ndarray are stored in a buffer which can be thought of as a contiguous block of memory bytes. So how these bytes will be interpreted is given by the dtype object.  
Constructing a data type (dtype) object : Data type object is an instance of numpy.dtype class and it can be created using numpy.dtype.


Parameters:
obj: Object to be converted to a data type object.
align : [bool, optional] Add padding to the fields to match what a C compiler would output for a similar C-struct.
copy : [bool, optional] Make a new copy of the data-type object. If False, the result may just be a reference to a built-in data-type object.

"""
import numpy as np
print(
    "------------------------------------------------------------------------------")

print(np.dtype(np.int32))

print("------------------------------------------------------------------------------")

# i4 represents integer of size 4 byte
# > represents big-endian byte ordering and
# < represents little-endian encoding.
# dt is a dtype object

dt = np.dtype('>i8')
print("Byte order : ", dt.byteorder)
print("Size : ", dt.itemsize)
print("Data type : ", dt.name)

"""
Note:
The type specifier (i4 in above case) can take different forms:

b1, i1, i2, i4, i8, u1, u2, u4, u8, f2, f4, f8, c8, c16, a (representing bytes, ints, unsigned ints, floats, complex and fixed length strings of specified byte lengths)

int8,…,uint8,…,float16, float32, float64, complex64, complex128 (this time with bit sizes)
"""

print("------------------------------------------------------------------------------")

var = np.array([1, 2, 3])
print("Type : ", type(var))
print("Dtype : ", var.dtype)

print("------------------------------------------------------------------------------")
# A structured data type containing a
# 16-character string (in field ‘name’) 
# and a sub-array of two 64-bit floating
# -point number (in field ‘grades’)
dt2 = np.dtype([
  ('name',np.unicode_,16),
  ('grades',np.float64,(2,))
 ])

print(dt2['name'])
print(dt2['grades'])
