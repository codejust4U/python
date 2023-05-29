"""
Dealing with Rows and Columns in Pandas DataFrame

A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming. In this article, we are using nba.csv file.

Dealing with Columns
In order to deal with columns, we perform basic operations on columns like selecting, deleting, adding and renaming.


Column Selection:
In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.
"""
import pandas as pd
print("-------------------------------Viewing Data------------------------------------")
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
dataframe1 = pd.DataFrame(data1)

print(dataframe1)
print("-------------------------------------------------------------------------------")

print(dataframe1[['Name','Age']])
print("-------------------------------------------------------------------------------")
print("-------------------------------Adding Data------------------------------------")
Course = ['BTCS','BTCE','BTME','BTEE']
dataframe1['Course'] = Course
print(dataframe1)
print("-------------------------------------------------------------------------------")

"""
Column Deletion:
In Order to delete a column in Pandas DataFrame, we can use the drop() method. Columns is deleted by dropping columns with column names.
"""
print("-------------------------------Dropping Column---------------------------------")
del data1['Address']
print(data1)

print("-------------------------------------------------------------------------------")

"""
Dealing with Rows:
In order to deal with rows, we can perform basic operations on rows like selecting, deleting, adding and renaming.

Row Selection:
Pandas provide a unique method to retrieve rows from a Data frame.DataFrame.loc[] method is used to retrieve rows from Pandas DataFrame. Rows can also be selected by passing integer location to an iloc[] function.
"""
print("------Before performing any operation--------------------")
data_read1 = pd.read_csv(r'D:\excel_datas\day4\nba.csv',index_col='Name')
print(data_read1)

print("------after performing operations--------------------")
first = data_read1.loc["Avery Bradley"]
second = data_read1.loc["R.J. Hunter"]

  
print(first, "\n\n\n", second)

print("--------Deleting a row from selected column-------")
del first['Height']
print(first)
print("--------Adding a row to selected index-------")

new_data = pd.DataFrame({
'Name' : 'Pankaj',
'Team' : 'SARI',
'Position' : 'UG',
'Age' : 22,
'weight' : '56',
'College' : 'KU',
'Salary' : '000'
},
index=[1])

dataframe1 = pd.concat([new_data]).reset_index(drop=True)
print(dataframe1)
print("-------------------------------------------------------------------------------")

"""
Python | Pandas Extracting rows using .loc[]

Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier.

Pandas provide a unique method to retrieve rows from a Data frame. DataFrame.loc[] method is a method that takes only index labels and returns row or dataframe if the index label exists in the caller data frame.

Syntax: pandas.DataFrame.loc[]

Parameters:
Index label: String or list of string of index label of rows


Return type: Data frame or Series depending on parameters
"""

