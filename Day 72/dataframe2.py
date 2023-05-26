"""
Iterating over Columns :
In order to iterate over columns, we need to create a list of dataframe columns and then iterating through that list to pull out the dataframe columns.
"""
import pandas as pd
import numpy as np

print("----------------------------------Data frame-----------------------------------")
data1 = {
    "name" : ["pankaj","ravi","amanuwell","subash","gulshan"],
    "rollno" : [50,59,9,65,34],
    "marks" : [40,99,98,97,96],
    "class" : ["first","first","second","second","first"]
}
dataframe1 = pd.DataFrame(data1)
column1 = list(dataframe1)
for i in column1:
    print(dataframe1[i])
print("-------------------------------------------------------------------------------")
print("---------------------------------Serial Data-----------------------------------")
serial_data = pd.Series(data1)
print(serial_data)

print("-------------------------------------------------------------------------------")

"""
Accessing element of Series
There are two ways through which we can access element of series, they are :

Accessing Element from Series with Position
Accessing Element Using Label (index)
Accessing Element from Series with Position : In order to access the series element refers to the index number. Use the index operator [ ] to access an element in a series. The index must be an integer. In order to access multiple elements from a series, we use Slice operation.
"""

print("---------------------------------Serial Data-----------------------------------")

dataframe2 = np.array(['p','a','n','k','a','j'])
serial_data2 = pd.Series(dataframe2)
print(serial_data2)

print("-------------------------------------------------------------------------------")

"""
Indexing and Selecting Data in Series
Indexing in pandas means simply selecting particular data from a Series. Indexing could mean selecting all the data, some of the data from particular columns. Indexing can also be known as Subset Selection.

Indexing a Series using indexing operator [] :
Indexing operator is used to refer to the square brackets following an object. The .loc and .iloc indexers also use the indexing operator to make selections. In this indexing operator to refer to df[ ].
"""
print("---------------------------------Indexing and Selectin Data-----------------------------------")

dataframe3 = pd.read_csv(r'D:\excel_datas\day1\students - Sheet1.csv')

serial_data3 = pd.Series(dataframe3['first_name'])
limit = serial_data3.head(10)
print(limit)
print("-------------------------------------------------------------------------------")

"""
By default, the index of the series starts from 0 till the length of series -1.

Creating a series from array with an index: In order to create a series by explicitly proving index instead of the default, we have to provide a list of elements to the index parameter with the same number of elements as it is an array. 
"""
print("---------------------------------Changing the index-----------------------------------")
dataframe3 = np.array(['p','a','n','k','a','j'])

serial_data4 = pd.Series(dataframe3,index=[21,22,23,24,25,26])
print(serial_data4)
print("-------------------------------------------------------------------------------")

"""
Creating a series using NumPy functions : In order to create a series using numpy function, we can use different function of numpy like numpy.linspace(), numpy.random.radn(). 
"""
print("---------------------------------Creating a series-----------------------------------")
serial_data5 = pd.Series(np.linspace(1,11,3))
print(serial_data5)
print("-------------------------------------------------------------------------------\n")
serial_data6 = pd.Series(np.linspace(0,50,10))
print(serial_data6)
print("-------------------------------------------------------------------------------")

print("----------------------------Creating a series with index in alphabet--------------------------")
serial_data7=pd.Series(range(1,40,6), index=[x for x in 'abcdefg'])
print(serial_data7)
print("-------------------------------------------------------------------------------")


serial_data8=np.arange(11,16)
serobj=pd.Series(data=serial_data8*8,index=serial_data8)
print(serobj)
print("-------------------------------------------------------------------------------")
