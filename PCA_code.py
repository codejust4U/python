import numpy as np
import pandas as pd


df =  pd.read_csv(r'D:\datas\excel\Day32 MNIST\digit-recognizer\train.csv')


print(df.shape)
print(df.head())
import matplotlib.pyplot as plt

plt.imshow(df.iloc[186,1:].values.reshape(28,28))

X= df.iloc[:,1:]
y=df.iloc[:,0]

from sklearn.model_selection import train_test_split


X_train, X_test, y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print(X_train.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

import time
start = time.time()
y_pred=knn.predict(X_test)

print(time.time()-start)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred))

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test=scalar.fit_transform(X_test)

from sklearn.decomposition import PCA

pca = PCA(n_components=200)
X_train_trf=pca.fit_transform(X_train)
X_test_trf= pca.fit_transform(X_test)

print(X_train_trf.shape)

knn = KNeighborsClassifier()
knn.fit(X_train_trf,y_train)
y_pred = knn.predict(X_test_trf)


accuracy_score(y_test,y_pred)


for i in range(1,10):
    pca=PCA(n_components=i)
    X_train_trf=pca.fit_transform(X_train)
    X_test_trf= pca.fit_transform(X_test)

    knn = KNeighborsClassifier()
    knn.fit(X_train_trf,y_train)
    y_pred = knn.predict(X_test_trf)

    print(i," ",(accuracy_score(y_test,y_pred)*100))
    

# transforming into a 2D

pca = PCA(n_components=2)
X_train_trf = pca.fit_transform(X_train)
X_test_trf=pca.fit_transform(X_test)


print(X_train_trf)

import plotly.express as px

y_train_trf = y_train.astype(str)
fig = px.scatter(x=X_train_trf[:,0],
                 y=X_train_trf[:,1],
                 color=y_train_trf,
                 color_discrete_sequence=px.colors.qualitative.G10)
fig.show()

# transforming into a 3D

pca = PCA(n_components=3)
X_train_trf = pca.fit_transform(X_train)
X_test_trf=pca.fit_transform(X_test)

print(X_train_trf)

y_train_trf=y_train.astype(str)
fig =px.scatter_3d(df,x=X_train_trf[:,0],y=X_train_trf[:,1],z=X_train_trf[:,2],
                   color=y_train_trf)
fig.update_layout(margin=dict(l=20,r=20,t=20,b=20))
fig.show()


print(pca.explained_variance_)

print(pca.components_)


pca = PCA(n_components=None)
X_train_trf = pca.fit_transform(X_train)
X_test_trf=pca.fit_transform(X_test)


plt.plot(np.cumsum(pca.explained_variance_ratio_))

plt.show()