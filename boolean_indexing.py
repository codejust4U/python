"""
Boolean Indexing in Pandas


In boolean indexing, we will select subsets of data based on the actual values of the data in the DataFrame and not on their row/column labels or integer locations. In boolean indexing, we use a boolean vector to filter the data.

Accessing a DataFrame with a boolean index: 
In order to access a dataframe with a boolean index, we have to create a dataframe in which the index of dataframe contains a boolean value that is “True” or “False”.
"""
import pandas as pd
dict1 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
print("-------------Accessing through Boolean Values----------------")
dataframe1 = pd.DataFrame(dict1, index = [True, False, True, False])

print(dataframe1)
print("--------------------------------------------------------")
"""
Accessing a Dataframe with a boolean index using .iloc[]
In order to access a dataframe using .iloc[], we have to pass a boolean value (True or False)  but iloc[] function accepts only integer as an argument so it will throw an error so we can only access a dataframe when we pass an integer in iloc[] function 
"""
print(dataframe1[dataframe1.index == True])


print("--------------------------------------------------------")

