import numpy as np
import pandas as pd

"""
Python | Pandas Dataframe/Series.head() method
Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier.

Pandas head() method is used to return top n (5 by default) rows of a data frame or series.

Syntax: Dataframe.head(n=5)

Parameters:
n: integer value, number of rows to be returned

Return type: Dataframe with top n rows
"""
data1 = pd.read_csv(r"https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

print(data1)

print("-------------------------------------------------------------------------------")

"""
In this example, top 5 rows of data frame are returned and stored in a new variable. No parameter is passed to .head() method since by default it is 5.
"""
top_data1 = data1.head(5)

print(top_data1)

print("-------------------------------------------------------------------------------")

"""
Calling on Series with n parameter()

In this example, the .head() method is called on series with custom input of n parameter to return top 9 rows of the series.
"""

"""n=9
series_data1 = data1["Name"]
top_data2 = series_data1.head(n==n)
print(top_data2)"""
print("-------------------------------------------------------------------------------")

"""
Python | Pandas Dataframe/Series.tail() method

Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier.

Pandas tail() method is used to return bottom n (5 by default) rows of a data frame or series.

Syntax: Dataframe.tail(n=5)

Parameters:
n: integer value, number of rows to be returned


Return type: Dataframe with bottom n rows
"""
print("-------------------------------------------------------------------------------")
data2 = pd.read_csv(r'https://media.geeksforgeeks.org/wp-content/uploads/nba.csv')

data_bottom1 = data2.tail()

print(data_bottom1)
print("-------------------------------------------------------------------------------")