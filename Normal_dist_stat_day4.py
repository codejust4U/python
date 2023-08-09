import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day126 EDA\Titanic-Dataset.csv')
print(df.head())


print(df['Age'].head())


import seaborn as sns


sns.kdeplot(df['Age'])
plt.show()


mean=df['Age'].mean()
std=df['Age'].std()
SND=(df['Age']-mean)/std

x=0
y=0.5
sns.kdeplot(SND)
plt.plot(x,y)
plt.show()


print("Very very close to zero or exact zero : ",SND.mean())


print(SND.std())


print(df['Age'].skew())


print(df['Age'].mean()+3*df['Age'].std())


print(df['Age'].mean()-3*df['Age'].std())



try:
    if df['Age']>73:
        print(df[df['Age']])
    elif df['Age']<-13:
        print(df[df['Age']])
    else:
        pass
except:
    pass


print(df[df['Age']>73])

# these 2 passengers doesn't come under 99.7% of passengers