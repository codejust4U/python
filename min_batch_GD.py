from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import time

X,y = load_diabetes(return_X_y=True)

print(X.shape)
print(y.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

reg = LinearRegression()

reg.fit(X_train,y_train)

print("Coefficient : ",reg.coef_)
print("\nIntercept : ",reg.intercept_)

y_pred = reg.predict(X_test)
print(r2_score(y_test,y_pred))

print(X_train.shape)