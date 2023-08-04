from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

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


class GDRegressor:
    def __init__(self,learning_rate=0.01,epochs=100):
        self.coef_=None
        self.intercept_=None
        self.lr= learning_rate
        self.epochs = epochs

    def fit(self,X_train,y_train):
        #init the coeffiecients
        self.intercept_=0
        self.coef_ = np.ones(X_train.shape[1])

        for i in range(self.epochs):
            # update coef abd intercept
            y_hat = np.dot(X_train,self.coef_)+self.intercept_
            #print("Shape if y_hat: ",y_hat.shape)
            intercept_der = -2*np.mean(y_train-y_hat)

            self.intercept_ = self.intercept_ - (self.lr* intercept_der)

            coef_der = -2 * np.dot((y_train-y_hat),X_train)/X_train.shape[0]

            self.coef_ = self.coef_ - (self.lr*coef_der)

        print("Intercept : ",self.intercept_,"\n","Coefficient : ",self.coef_)
        

    def predict(self,X_test):
        return np.dot(X_test,self.coef_)+self.intercept_
    

gdr = GDRegressor(epochs=1000,learning_rate=0.5)

gdr.fit(X_train,y_train)

y_pred = gdr.predict(X_test)

print(r2_score(y_test,y_pred))