#importing the modules
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


#fetching the 
iris = datasets.load_iris()

#splitting into X and y
X = iris.data
y = iris.target

classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = svm.SVC()
model.fit(X_train, y_train)

print(model)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Predictions: ", predictions)
print("Accuracy: ", accuracy)


for i in range(len(predictions)):
    print(classes[predictions[i]])