
# importing pandas module
import re
import pandas as pd
print("--------------------------Bottom_data-------------------------")
# making data frame
data = pd.read_csv(r'D:\excel_datas\day4\nba.csv')

# number of rows to return
n = 12

# creating series
series = data["Salary"]

# returning top n rows
bottom = series.tail(n=n)

print(bottom)
print("--------------------------------------------------------------")

"""
Pandas DataFrame describe() Method
Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier. 

Pandas DataFrame describe()
Pandas describe() is used to view some basic statistical details like percentile, mean, std, etc. of a data frame or a series of numeric values. When this method is applied to a series of strings, it returns a different output which is shown in the examples below.

Syntax: DataFrame.describe(percentiles=None, include=None, exclude=None) 

Parameters: 

percentile: list like data type of numbers between 0-1 to return the respective percentile 
include: List of data types to be included while describing dataframe. Default is None 
exclude: List of data types to be Excluded while describing dataframe. Default is None 
Return type: Statistical summary of data frame.
"""
print("-----------------------Describe behaviour---------------------")

# removing null
data.dropna(inplace=True)

# list of percentag
percentile1 = [.30, .40, .60]
include1 = ['object', 'float', 'int']

describe1 = data.describe(percentiles=percentile1, include=include1)

print(describe1)
print("--------------------------------------------------------------")

describe2 = data["Name"].describe()
print(describe2)

print("--------------------------------------------------------------")

"""
Pandas Dataframe.to_numpy() – Convert dataframe to Numpy array

Pandas DataFrame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). This data structure can be converted to NumPy ndarray with the help of the DataFrame.to_numpy() method. In this article we will see how to convert dataframe to numpy array.

Syntax of Pandas DataFrame.to_numpy()
Syntax: Dataframe.to_numpy(dtype = None, copy = False) 

Parameters: 

dtype: Data type which we are passing like str. 
copy: [bool, default False] Ensures that the returned value is a not a view on another array.
Returns: numpy.ndarray
"""
dataframe1 = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
], columns=['a', 'b', 'c'])
print("-------------------Dataframe to Numpy-------------------------")
array1 = dataframe1.to_numpy()
print(array1)
print(type(array1))

print("--------------------------------------------------------------")
print("-----------------Dataframe to Numpy -2 column-----------------")
array2 = dataframe1[['a', 'b']].to_numpy()
print(array2)

print("-----------------------reading scv ---------------------------")

data_read1 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')
print(data_read1)
print("----------------------show specific column--------------------")
data_read1.dropna(inplace=True)
dataframe2 = pd.DataFrame(data['Weight'].head())

print(dataframe2.to_numpy())
print("-------------------------with dtype --------------------------")

print(dataframe2.to_numpy(dtype='float32'))
print("--------------------------------------------------------------")

print(type(dataframe2.to_numpy(dtype='float32')))
print("--------------------------------------------------------------")

"""
Python | Pandas Series.to_numpy()

Pandas Series.to_numpy() function is used to return a NumPy ndarray representing the values in given Series or Index.

This function will explain how we can convert the pandas Series to numpy Array. Although it’s very simple, but the concept behind this technique is very unique. Because we know the Series having index in the output. Whereas in numpy arrays we only have elements in the numpy arrays.

Syntax: Series.to_numpy()

Parameters:
dtype: Data type which we are passing like str.
copy : [bool, default False] Ensures that the returned value is a not a view on another arra
"""

data_in_series = pd.Series(data_read1['Weight'].head())
print(data_in_series.to_numpy())
print("--------------------------------------------------------------")

print(type(data_in_series.to_numpy()))
print("--------------------------------------------------------------")
"""
Python | Pandas Series.as_matrix()

Pandas series is a One-dimensional ndarray with axis labels. The labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index.

Pandas Series.as_matrix() function is used to convert the given series or dataframe object to Numpy-array representation.

Syntax: Series.as_matrix(columns=None)

Parameter :
columns : If None, return all columns, otherwise, returns specified columns.
"""

print("--------------Python | Pandas Series.as_matrix()--------------")
# Creating the Series
data_in_series2 = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio'])
  
# Create the Index
cities = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5'] 

data_in_series2.index = cities

print(data_in_series2)
print("--------------------------------------------------------------")



"""# return numpy array representation
result = data_in_series2.as_matrix()
  
# Print the result
print(result)"""


# Creating the Series
data_in_series3 = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None])
  
index_ = pd.date_range('2010-10-09 08:45',periods=11,freq='Y')

data_in_series3.index = index_

print(data_in_series3)
print("--------------------------------------------------------------")

"""result = data_in_series3.as_matrix()

print(result)"""
