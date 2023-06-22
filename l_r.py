import pandas as pd 
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.linear_model import LinearRegression


soap_sale = pd.read_excel(r'D:\datas\excel\day12\datas_.xlsx')
print(soap_sale.head())

print("-----------------------------")
x=soap_sale['No_of_shop']
y=soap_sale['disount_percent']
plt.scatter(x,y)
plt.title('no_of_soap vs discount_percent')
plt.xlabel("discount percent")
plt.ylabel("no of shops")

plt.show()

print("----------------------------")
X = soap_sale.iloc[:, :-1].values 
y = soap_sale.iloc[:, 1].values 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 
regressor = LinearRegression() 
regressor.fit(X_train, y_train) 
print(regressor.intercept_) 
print(regressor.coef_) 
y_pred = regressor.predict(X_test) 
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}) 
print(df)


print("----------------------------")


print("Mean Absolute error: ",metrics.mean_absolute_error(y_test,y_pred))

print("Mean Squaed error: ",metrics.mean_squared_error(y_test,y_pred))

print("Root mean sqaured error: ",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


