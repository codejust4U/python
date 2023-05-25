"""
Python Pandas DataFrame

Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components, the data, rows, and columns.
"""
"""
Creating a Pandas DataFrame
In the real world, a Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file. Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc. Dataframe can be created in different ways here are some ways by which we create a dataframe:

Creating a dataframe using List: DataFrame can be created using a single list or a list of lists.
"""

import pandas as pd
print("--------------------------Creating a dataframe in pandas------------------------")
# Creating a DataFrame using a list
list1 = ['pankaj','ravi','subash','amanuwell','gulshan','naman','samir','rahul']

dataframe1 = pd.DataFrame(list1)
print(dataframe1)
print("--------------------------------------------------------------------------------")

print("--------------------------With more than one attribute--------------------------")
list2 = {
    'Name' : ['pankaj','ravi','subash','amanuwell','gulshan','naman','samir','rahul'],
    'Age' : [23,22,21,23,22,20,22,20],
    'Id' : [11,12,13,14,15,16,17,18]
}
dataframe2 = pd.DataFrame(list2)
print(dataframe2)
print("--------------------------------------------------------------------------------")
"""
Dealing with Rows and Columns
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.

Column Selection: In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.
"""
print("--------------------------Dealing with rows and columns-------------------------")
list3 = {
    'Name' : ['pankaj','ravi','subash','amanuwell','gulshan','naman','samir','rahul'],
    'Age' : [23,22,21,23,22,20,22,20],
    'Id' : [11,12,13,14,15,16,17,18]
}
dataframe3 = pd.DataFrame(list3)
print("-------------------------------Printing only ages-------------------------------")
print(dataframe3[['Age']])
print("--------------------------------------------------------------------------------")

"""
Row Selection: Pandas provide a unique method to retrieve rows from a Data frame. DataFrame.loc[] method is used to retrieve rows from Pandas DataFrame. Rows can also be selected by passing integer location to an iloc[] function.

Note: We’ll be using nba.csv file in below examples.
"""
try:

    datas = pd.read_csv("datas1.csv",index_col="Name")
    first = datas.loc["Eli"]
    second = datas.loc["Jose Wong"]
    print(first,"\n\n",second)
except:
    print("File not found")

