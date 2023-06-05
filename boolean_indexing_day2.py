"""
Applying a boolean mask to a dataframe : 
In a dataframe, we can apply a boolean mask. In order to do that we can use __getitems__ or [] accessor. We can apply a boolean mask by giving a list of True and False of the same length as contain in a dataframe. When we apply a boolean mask it will print only that dataframe in which we pass a boolean value True. 
"""
import pandas as pd

data1 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

dataframe1 = pd.DataFrame(data1,index=[0,1,2,3])

print(dataframe1[[False,True,True,True]])



print("---------------------------------------------------------------------------")

data2 = pd.read_csv(r'D:\excel_datas\day4\nba.csv')

dataframe2 = pd.DataFrame(data2, index = [0, 1, 2, 3, 4, 5, 6,
                                 7, 8, 9, 10, 11, 12])

print(dataframe2)

print("---------------------------------------------------------------------------")

data3 = pd.read_csv(r'D:\excel_datas\day4\nba.csv',index_col='Name')

print(data3['Age']>25)

print("---------------------------------------------------------------------------")

