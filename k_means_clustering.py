import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

cancer = load_breast_cancer()

X = scale(cancer.data)
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = KMeans(n_clusters=2, random_state=0)
model.fit(X_train)

predictions = model.predict(X_test)
labels = model.labels_

print("labels: ", labels)
print("Predictions: ", predictions)
print("Accuracy: ", accuracy_score(y_test, predictions))
print("Actual: ", y_test)

def bench_k_means(estimator, name, data, labels):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
            metrics.homogeneity_score(labels, estimator.labels_),
            metrics.completeness_score(labels, estimator.labels_),
            metrics.v_measure_score(labels, estimator.labels_),
            metrics.adjusted_rand_score(labels, estimator.labels_),
            metrics.adjusted_mutual_info_score(labels, estimator.labels_),
            metrics.silhouette_score(data, estimator.labels_,
                                     metric='euclidean')))

bench_k_means(model, "1", X_train, y_train)


