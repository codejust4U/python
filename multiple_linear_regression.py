#Importing the modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Reading the data
read_data = pd.read_csv(r"D:\datas\excel\day13\advertising.csv")

print("\n-----------------------------")
print(read_data.head(5))

# Assigning x and y
x = read_data[['TV', 'Radio']]
y = read_data[['Sales']]

# Splitting the data
train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=100)

# Linear model implementation
lm = LinearRegression()
lm.fit(train_x, train_y)

print("\n-----------------------------")
# For intercept and coefficients
print("Intercept: ", lm.intercept_)
print("Coefficients: ", list(zip(x, lm.coef_)))

print("\n-----------------------------")

# Regression equation for sales
# Prediction on the test data
prdct = lm.predict(test_x)
print("The prediction based on the dependent value:", prdct, end=" ")

print("\n-----------------------------")

mlr_diff = pd.DataFrame({"actual value": test_y.values.flatten(), "Predicted value": prdct.flatten()})
mlr_diff.head()


print("\n-----------------------------")

from sklearn import metrics
meanAbErr = metrics.mean_absolute_error(test_y, prdct)
meanSqErr = metrics.mean_squared_error(test_y, prdct)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(test_y, prdct))
print('R squared: {:.2f}'.format(lm.score(x,y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)