"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the iris dataset from scikit-learn
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM classifier
svm = SVC()

# Train the classifier on the training data
svm.fit(X_train, y_train)

# Make predictions on the test data
y_pred = svm.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy)
"""


import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


cancer =  datasets.load_breast_cancer()


print("Features : ",cancer.feature_names)

# 0 - malignant and 1 - benign
print("\nLabels : ",cancer.target_names)

cancer.data.shape

print(cancer.data[:5])

print("1 - benign \t  0 - malignat\n")
print(cancer.target)

X_train, X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)

clf = svm.SVC(kernel='linear')

clf.fit(X_train,y_train)


y_pred = clf.predict(X_test)

print("\n\naccuracy  : ",metrics.accuracy_score(y_test,y_pred))