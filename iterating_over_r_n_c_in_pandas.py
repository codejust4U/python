"""
Iterating over rows and columns in Pandas DataFrame

Iteration is a general term for taking each item of something, one after another. Pandas DataFrame consists of rows and columns so, in order to iterate over dataframe, we have to iterate a dataframe like a dictionary. In a dictionary, we iterate over the keys of the object in the same way we have to iterate in dataframe.
"""

"""
In this article, we are using “nba.csv” file to download the CSV, click here.
In Pandas Dataframe we can iterate an element in two ways: 

Iterating over rows
Iterating over columns 
Iterating over rows :
In order to iterate over rows, we can use three function iteritems(), iterrows(), itertuples() . These three function will help in iteration over rows.  


Iteration over rows using iterrows()
In order to iterate over rows, we apply a iterrows() function this function returns each index value along with a series containing the data in each row.
"""

import pandas as pd
data1 = pd.read_csv(r'D:\excel_datas\day1\students - Sheet1.csv')

df1 = pd.DataFrame(data1)

print(df1)
print("------------------------------------------------------------------------")
for i,j in df1.iterrows():
    print(i,j)
    print()

print("------------------------------------------------------------------------")

data2 = pd.read_csv(r'D:\excel_datas\day1\students - Sheet1.csv')

df2 = pd.DataFrame(data2)
for i,j in df2.iterrows():
    print(i,j)
    print()
print("------------------------------------------------------------------------")
df3 = data2.head(10)
print(df3)
print("------------------------------------------------------------------------")
for i, j in df3.iterrows():
    print(i,j)
    print()

print("------------------------------------------------------------------------")


"""
Iteration over rows using iteritems()
In order to iterate over rows, we use iteritems() function this function iterates over each column as key, value pair with the label as key, and column value as a Series object.
"""

data3= {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df4 = pd.DataFrame(data3)
for key,value in df4.iterrows():
    print(key,value)
    print()
    
print("------------------------------------------------------------------------")
data4 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')

data4.head(5)

print("------------------------------------------------------------------------")

"""
Iteration over rows using itertuples()
In order to iterate over rows, we apply a function itertuples() this function return a tuple for each row in the DataFrame. The first element of the tuple will be the row’s corresponding index value, while the remaining values are the row values.
"""

data5 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df5 = pd.DataFrame(data5)

for i in df5.itertuples():
    print(i)

print("------------------------------------------------------------------------")

data6 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')

df6 = pd.DataFrame(data6)

print(df6.head(5))

for i in df6.itertuples():
    print(i)



print("------------------------------------------------------------------------")