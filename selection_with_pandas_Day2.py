"""
Selecting multiple rows
In order to select multiple rows, we can pass a list of integer to .iloc[] function.
"""

import pandas as pd
print("-------------------------Selecting multi rows-------------------------")
data1 = pd.read_csv(r'D:\excel_datas\day4\nba.csv',index_col='Name')
multi_row1 = data1.iloc[[2,5,8]]
print(multi_row1)

print("-------------------------------------------------------------------------------")

"""
In order to select two rows and two columns, we create a list of 2 integer for rows and list of 2 integer for columns then pass to a .iloc[] function.

"""

data_row_1 = data1.iloc[[2,3],[1,4]]

print(data_row_1)

print("-------------------------------------------------------------------------------")
"""
Selecting all the rows and a some columns
In order to select all rows and some columns, we use single colon [:] to select all of rows and for columns we make a list of integer then pass to a .iloc[] function.
"""
row_data_all = data1.iloc [:, [1, 2]]
print(row_data_all)

print("-------------------------------------------------------------------------------")

"""
Indexing a using Dataframe.ix[ ] :
Early in the development of pandas, there existed another indexer, ix. This indexer was capable of selecting both by label and by integer location. While it was versatile, it caused lots of confusion because it’s not explicit. Sometimes integers can also be labels for rows or columns. Thus there were instances where it was ambiguous. Generally, ix is label based and acts just as the .loc indexer. However, .ix also supports integer type selections (as in .iloc) where passed an integer. This only works where the index of the DataFrame is not integer based .ix will accept any of the inputs of .loc and .iloc.
Note: The .ix indexer has been deprecated in recent versions of Pandas.

Selecting a single row using .ix[] as .loc[]
In order to select a single row, we put a single row label in a .ix function. This function act similar as .loc[] if we pass a row label as a argument of a function.
"""

