"""
Read csv using pandas.read_csv() in Python

To access data from the CSV file, we require a function read_csv() that retrieves data in the form of the data frame.

Syntax of read_csv() 
Here is the Pandas read CSV syntax with its parameter.

Syntax: pd.read_csv(filepath_or_buffer, sep=’ ,’ , header=’infer’,  index_col=None, usecols=None, engine=None, skiprows=None, nrows=None) 

Parameters: 

filepath_or_buffer: It is the location of the file which is to be retrieved using this function. It accepts any string path or URL of the file.
sep: It stands for separator, default is ‘, ‘ as in CSV(comma separated values).
header: It accepts int, a list of int, row numbers to use as the column names, and the start of the data. If no names are passed, i.e., header=None, then,  it will display the first column as 0, the second as 1, and so on.
usecols: It is used to retrieve only selected columns from the CSV file.
nrows: It means a number of rows to be displayed from the dataset.
index_col: If None, there are no index numbers displayed along with records.  
skiprows: Skips passed rows in the new data frame.
Read CSV File using Pandas read_csv
Before using this function, we must import the Pandas library, we will load the CSV file using Pandas.
"""

import pandas as pd
print(pd.read_csv(r'D:\excel_datas\day5\employees.csv'))

