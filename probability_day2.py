import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the data into train and test DataFrames
train = pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day156 Statistics_day9\train.csv')
test = pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day156 Statistics_day9\test.csv')

# Concatenate the train and test DataFrames to create a new DataFrame 'df'
df = pd.concat([train, test]).sample(1309)


print(pd.crosstab(df['Survived'],df['Pclass']))

# joint probability
print(pd.crosstab(df['Survived'],df['Pclass'],normalize='all'))

# marginal probability
print(pd.crosstab(df['Survived'],df['Pclass'],normalize='all',margins=True))

# conditional probability for P(Y/X)
print(pd.crosstab(df['Survived'],df['Pclass'],normalize='columns'))

# conditional probability for P(X/Y)
print(pd.crosstab(df['Survived'],df['Pclass'],normalize='index'))