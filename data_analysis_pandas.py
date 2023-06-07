"""
Data analysis using Pandas

Pandas are the most popular python library that is used for data analysis. It provides highly optimized performance with back-end source code purely written in C or Python. 

We can analyze data in Pandas with:

Pandas Series
Pandas DataFrames
Pandas Series
Series in Pandas is one dimensional(1-D) array defined in pandas that can be used to store any data type.

Creating Pandas Series


Here, Data can be:

A Scalar value which can be integerValue, string
A Python Dictionary which can be Key, Value pair
A Ndarray
Note: Index by default is from 0, 1, 2, …(n-1) where n is the length of data.  

Create Series from List
 Creating series with predefined index values.
"""

import pandas as pd
Data = [1,4,6,2,8,3,9]
series1 = pd.Series(Data)
Index = ['a','b','c','d','e','f','g']
ser1 = pd.Series(Data,Index)
print(ser1)

print("------------------------------------------------------------")

"""
Create Pandas Series from Dictionary
Program to Create Pandas series from Dictionary.
"""
dict1 = {
    'a':'pankaj',
    'b':'ravi',
    'c':'subash',
    'd':'amanuwell'     
         }

series2 = pd.Series(dict1)

print(series2)
print("------------------------------------------------------------")
"""
Pandas DataFrames
The DataFrames in Pandas is a two-dimensional (2-D) data structure defined in pandas which consists of rows and columns.

Here, Data can be:

One or more dictionaries
One or more Series
2D-numpy Ndarray
Create a Pandas DataFrame from multiple Dictionary
Program to Create a Dataframe with two dictionaries.

"""


dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict3 = {'a': 5, 'b': 6, 'c': 7, 'd': 8, 'e': 9}

data2 = {'1st row' : dict2,'2nd row' : dict3}

df2 = pd.DataFrame(data2)
print(df2)
print("------------------------------------------------------------")


"""
Convert list of dictionaries to a Pandas DataFrame
Here, we are taking three dictionaries and with the help of from_dict() we convert them into Pandas DataFrame.
"""

data3 = [
 {'A': 5, 'B': 0, 'C': 3, 'D': 3},
 {'A': 7, 'B': 9, 'C': 3, 'D': 5},
 {'A': 2, 'B': 4, 'C': 7, 'D': 6}]

print(pd.DataFrame.from_dict(data3,orient='columns'))

print("------------------------------------------------------------")