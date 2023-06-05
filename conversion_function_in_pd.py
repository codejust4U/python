"""
Conversion Functions in Pandas DataFrame

Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric python packages. Pandas is one of those packages and makes importing and analyzing data much easier. 
"""

"""
Cast a pandas object to a specified dtype
DataFrame.astype() function is used to cast a pandas object to a specified dtype. astype() function also provides the capability to convert any suitable existing column to categorical type.

Code #1: Convert the Weight column data type.
"""

import pandas as pd

df1 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')
  
df1[:10]

"""
Infer better data type for input object column
DataFrame.infer_objects() function attempts to infer better data type for input object column. This function attempts soft conversion of object-dtyped columns, leaving non-object and unconvertible columns unchanged. The inference rules are the same as during normal Series/DataFrame construction.

Code #1: Use infer_objects() function to infer better data type.
"""


"""
Detect missing values
DataFrame.isna() function is used to detect missing values. It return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, gets mapped to True values. Everything else gets mapped to False values. Characters such as empty strings ” or numpy.inf are not considered NA values (unless you set pandas.options.mode.use_inf_as_na = True).
"""
import pandas as pd

df5 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')

print(df5)
print("-----------------------------------------------------------------")
df5.isna()
"""
Detecting existing/non-missing values
DataFrame.notna() function detects existing/ non-missing values in the dataframe. The function returns a boolean object having the same size as that of the object on which it is applied, indicating whether each individual value is a na value or not. All of the non-missing values gets mapped to true and missing values get mapped to false.
"""
import pandas as pd

df5 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')

df5.notna()

print("-----------------------------------------------------------------")

"""
Methods for conversion in DataFrame
Function	Description
DataFrame.convert_objects()	Attempt to infer better dtype for object columns.
DataFrame.copy()	Return a copy of this object’s indices and data.
DataFrame.bool()	Return the bool of a single element PandasObject.
"""