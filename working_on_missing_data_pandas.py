"""
Working with Missing Data in Pandas

Missing Data can occur when no information is provided for one or more items or for a whole unit. Missing Data is a very big problem in a real-life scenarios. Missing Data can also refer to as NA(Not Available) values in pandas. In DataFrame sometimes many datasets simply arrive with missing data, either because it exists and was not collected or it never existed. For Example, Suppose different users being surveyed may choose not to share their income, some users may choose not to share the address in this way many datasets went missing.

Pandas treat None and NaN as essentially interchangeable for indicating missing or null values. To facilitate this convention, there are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :

isnull()
notnull()
dropna()
fillna()
replace()
interpolate()


Checking for missing values using isnull() and notnull()
In order to check missing values in Pandas DataFrame, we use a function isnull() and notnull(). Both function help in checking whether a value is NaN or not. These function can also be used in Pandas Series in order to find null values in a series.

Checking for missing values using isnull()
In order to check null values in Pandas DataFrame, we use isnull() function this function return dataframe of Boolean values which are True for NaN values.
"""

import numpy as np
import pandas as pd
data1= {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

df1 = pd.DataFrame(data1)

print(df1.isnull())

print("-----------------------------------------------------------------------------")

data2 = pd.read_csv(r'D:\excel_datas\day5\employees.csv')

bool_s_1 = pd.isnull(data2["Gender"])
print(data2[bool_s_1])

print("-----------------------------------------------------------------------------")

"""
Checking for missing values using notnull()
In order to check null values in Pandas Dataframe, we use notnull() function this function return dataframe of Boolean values which are False for NaN values.
"""

data3 = pd.read_csv(r'D:\excel_datas\day5\employees.csv')

bool_s_2 = pd.notnull(data3["Gender"])

print(bool_s_2)
print("-----------------------------------------------------------------------------")

"""
Filling missing values using fillna(), replace() and interpolate()
In order to fill null values in a datasets, we use fillna(), replace() and interpolate() function these function replace NaN values with some value of their own. All these function help in filling a null values in datasets of a DataFrame. Interpolate() function is basically used to fill NA values in the dataframe but it uses various interpolation technique to fill the missing values rather than hard-coding the value.
"""

"""data4 = pd.read_csv(r'D:\excel_datas\day5\employees.csv')

bool_s_3 = pd.DataFrame(data4)

print(bool_s_3.fillna(0))"""

print("-----------------------------------------------------------------------------")

data4 = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
bool_s_3 = pd.DataFrame(data4)

print(bool_s_3.fillna(0))
print("-----------------------------------------------------------------------------")
print(bool_s_3.fillna(method='pad'))
print("-----------------------------------------------------------------------------")

"""
Now we are going to fill all the null values in Gender column with “No Gender”
"""
data5 = pd.read_csv(r'D:\excel_datas\day5\employees.csv')

data5["Gender"].fillna("No gender", inplace=True)

print(data5)

print("-----------------------------------------------------------------------------")