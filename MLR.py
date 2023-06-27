"""
Regression models are used to describe relationships between variables by fitting a line to the observed data. Regression allows you to estimate how a dependent variable changes as the independent variable(s) change.

In multple linear regression, simlpy means there can be multiple independent varibale, so on the change of those IVs, how the dependent variables. This relation is basically Multiple linear regression (MLR).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataset = pd.read_csv('D:\datas\excel\Day16\multiple_lr.csv')


x=dataset.iloc[:,:-1]
y=dataset.iloc[:,4]
"""from sklearn.linear_model import LinearRegression

X = x.apply(pd.to_numeric, errors='coerce')
Y = y.apply(pd.to_numeric, errors='coerce')"""
x = x.apply(pd.to_numeric, errors='coerce')
y = y.apply(pd.to_numeric, errors='coerce')

x.fillna(0, inplace=True)
y.fillna(0, inplace=True)


states = pd.get_dummies(['State'],drop_first=True)


x=pd.concat([x,states],axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


from sklearn.metrics import r2_score
y_pred= regressor.predict(x_test)

#plt.plot(x_train,y_train)


scre = r2_score(y_test,y_pred)
plt.plot(y_test,y_pred)
plt.scatter(dataset['R&D Spend'],dataset['Profit'])
plt.xlabel("R&D spend and Y-test")
plt.ylabel("Profit and Y-predict")
plt.title("R&D spend Vs Profit Scattered \n Line plot of Y-test VS Y-predict",fontname="Blackadder ITC",fontsize='20')
plt.show()
print("The R-squared score is : ", scre)



x1 = dataset['Administration']
x2 = dataset['Marketing Spend']
y1 = dataset['Profit']
x3=(0,350000)
y3=(35000,200000)
plt.scatter(x1,y1)
plt.scatter(x2,y1)
plt.plot(x3,y3,'g')
plt.plot()
plt.xlabel("Administration")
plt.ylabel("Price")
plt.title("Administration VS Price Plot",fontname="Blackadder ITC",fontsize='20')
plt.show()