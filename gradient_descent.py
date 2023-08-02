from sklearn.datasets import make_regression
import numpy as np

X,y = make_regression(n_samples=4,n_features=1,n_informative=1,n_targets=1,noise=80,random_state=13)

import matplotlib.pyplot as plt
plt.scatter(X,y)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X,y)

reg.coef_

reg.intercept_

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue')

y_pred = ((78.35*X)+0).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred,color='red',label='b=0')
plt.legend


m=78.35
b=0
loss_slope = -2 * np.sum(y-m*X.ravel()-b)
loss_slope


# taking learning rate = 0.1
lr=0.1

step_size=loss_slope*lr
step_size


b=b-step_size
b

y_pred1= ((78.35*X)+b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred1,color='red',label='b={}'.format(b))
plt.plot(X,y_pred,color='green',label='b=0')
plt.legend()

# 2nd Iteration
loss_slope = -2 * np.sum(y-m*X.ravel()-b)
loss_slope


step_size=loss_slope*lr
step_size

b=b-step_size
b

y_pred2= ((78.35*X)+b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred2,color='purple',label='b={}'.format(b))
plt.plot(X,y_pred1,color='red',label='b={}'.format(b))
plt.plot(X,y_pred,color='green',label='b=0')
plt.legend()

# 3rd Iteration
loss_slope = -2 * np.sum(y-m*X.ravel()-b)
loss_slope

step_size=loss_slope*lr
step_size


b=b-step_size
b

y_pred3= ((78.35*X)+b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred2,color='gold',label='b={}'.format(b))
plt.plot(X,y_pred2,color='purple',label='b={}'.format(b))
plt.plot(X,y_pred1,color='red',label='b={}'.format(b))
plt.plot(X,y_pred,color='green',label='b=0')
plt.legend()


y_pred = ((78.35*X)+100).reshape(4)



plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred,color='red',label='b=0')
plt.legend

m=78.35
b=100
loss_slope = -2 * np.sum(y-m*X.ravel()-b)
loss_slope

# taking learning rate = 0.1
lr=0.1

step_size=loss_slope*lr
step_size

b=b-step_size
b


y_pred1= ((78.35*X)+b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred1,color='red',label='b={}'.format(b))
plt.plot(X,y_pred,color='green',label='b=0')
plt.legend()

# 2nd Iteration
loss_slope = -2 * np.sum(y-m*X.ravel()-b)
loss_slope

step_size=loss_slope*lr
step_size

b=b-step_size
b

y_pred2= ((78.35*X)+b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred2,color='purple',label='b={}'.format(b))
plt.plot(X,y_pred1,color='red',label='b={}'.format(b))
plt.plot(X,y_pred,color='green',label='b=0')
plt.legend()

# 3rd Iteration
loss_slope = -2 * np.sum(y-m*X.ravel()-b)
loss_slope


step_size=loss_slope*lr
step_size

b=b-step_size
b

y_pred3= ((78.35*X)+b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='blue',label='OLS')
plt.plot(X,y_pred2,color='gold',label='b={}'.format(b))
plt.plot(X,y_pred2,color='purple',label='b={}'.format(b))
plt.plot(X,y_pred1,color='red',label='b={}'.format(b))
plt.plot(X,y_pred,color='green',label='b=0')
plt.legend()


b=-100
m=78.35
lr=0.01

epochs = 100
for i in range(epochs):
    loss_slope = -2*np.sum(y-m*X.ravel()-b)
    b=b-(lr*loss_slope)

    y_pred=m*X+b
    plt.plot(X,y_pred)
    plt.scatter(X,y)



X,y = make_regression(n_samples=100,n_features=1,n_informative=1,n_targets=1,noise=20)
plt.scatter(X,y)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X,y)
print(lr.coef_)
print(lr.intercept_)

m=29.19

class GDRegressor:
    def __init__(self,learning_rate,epochs):
        self.m = 29.19
        self.b=-120
        self.lr=learning_rate
        self.epochs=epochs

    def fit(self,X,y):
        # calculate the b usig GD
        for i in range(self.epochs):
            loss_slope=-2*np.sum(y-self.m*X.ravel()-self.b)
            self.b=self.b-(self.lr*loss_slope)
            print(loss_slope,"\t",self.b)
        print(self.b)


gd = GDRegressor(0.001,100)

print(gd.fit(X,y))