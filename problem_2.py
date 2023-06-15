import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.DataFrame({
    'Bedrooms': [3, 4, 2, 5, 3],
    'Living Area': [1500, 2000, 1200, 3000, 1800],
    'Location': ['Urban', 'Suburban', 'Rural', 'Suburban', 'Urban'],
    'Age': [5, 10, 15, 2, 8],
    'Price': [250000, 400000, 150000, 600000, 350000]
})

dataset = pd.get_dummies(dataset, columns=['Location'])


X = dataset.drop('Price', axis=1)
y = dataset['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()


model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

"""
from sklearn.metrics import r2_score

# Assuming your predictions and actual values are stored in y_pred and y_actual, respectively

if len(y_test) >= 2:
    r2 = r2_score(y_test, y_pred)
    print("R^2 score:", r2)
else:
    print("Insufficient data to calculate R^2 score.")"""



new_data = pd.DataFrame({
    'Bedrooms': [4],
    'Living Area': [2200],
    'Location_Suburban': [1],
    'Location_Urban': [0],
    'Age': [7]
})
new_prediction = model.predict(new_data)
print("Predicted Price for new house:", new_prediction)
"""
import pandas as pd

new_data = pd.DataFrame({
    'Bedrooms': [4],
    'Living Area': [2200],
    'Location_Suburban': [1],
    'Location_Urban': [0],
    'Location_Rural': [0],  # Add Location_Rural feature
    'Age': [7]
})
new_prediction = model.predict(new_data)
print("Predicted Price for new house:", new_prediction)"""

