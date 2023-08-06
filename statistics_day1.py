import numpy as np
import pandas as pd

df=pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day147 Statistics-Day1\Titanic-Dataset.csv')
df.head()

import matplotlib.pyplot as plt

df['Fare'].plot(kind='hist')
plt.show()


print(df['Fare'].describe())


plt.hist(df['Fare'])
plt.show()

df['Fare'].plot(kind='box')
plt.show()


df['Fare'].plot(kind='area')
plt.show()

print(df['Fare'].skew)

df['Fare'].plot(kind='kde')
plt.show()


print(df['Fare'].isnull().sum()/len(df['Fare']))
df.head()



df['Cabin'].value_counts().plot(kind='pie',autopct='%0.2f%%')
plt.show()

df['Fare'].value_counts().plot(kind='pie',autopct='%0.2f%%')
plt.show()

df['SibSp'].value_counts().plot(kind='pie',autopct='%0.2f%%',explode=[0,0,0.1,0.2,0.3,0.4,0.5])
plt.show()


df['Age'].value_counts().plot(kind='pie',autopct='%0.2f%%')
plt.show()


plt.plot(df['PassengerId'],df['Survived'])
plt.show()



df['Parch'].value_counts().plot(kind='pie',autopct='%.2f%%',explode=[0,0,0,0.5,0.5,0.5,0.5])
plt.show()

df['Embarked'].value_counts().plot(kind='pie',autopct='%0.2f%%')
plt.show()

df.head()

print(pd.crosstab(df['Age'],df['Sex']))


import seaborn as sb

sb.heatmap(pd.crosstab(df['Age'],df['Sex']))
plt.show()

