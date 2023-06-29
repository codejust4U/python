# Normal plot for the Equations - 1


import matplotlib.pyplot as plt

x=[i for i in range(10)]

y=[2+3*i for i in range(10)]

plt.title("Linear plotting for Y=2+3x",fontname='Harlow Solid Italic',fontsize=20)
plt.scatter(x,y,color='red')
plt.plot(x,y)



# Training the modek

# Dont run it
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import os
import joblib

X = []
y = []

scaler = StandardScaler()

for j in range(9):
    files = os.listdir()
    len_f = len(files)
    for i in range(len_f):
        img = Image.open('{}{}'.format(j, files[i]))
        data = np.array(list(img.getdata())) / 255
        X.append(data.tolist())
        y.append(j)

print("Final X:", X)

# neural network
clf = MLPClassifier(solver="adam", activation="relu", alpha=1e-5, hidden_layer_sizes=(400, 2400), random_state=2)
print(clf)

# splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

# training the model
print("Training the model...")
clf.fit(X_train, y_train)

# saving
filename = 'model.joblib'
joblib.dump(clf, filename)

# predictions
print("Predictions:", clf.predict(X_test))




#Train test split

from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
#splitting the datas
X2 = iris.data
y2 = iris.target
print(X2.shape)
print(y2.shape)



#New model

from sklearn.model_selection import train_test_split

X_train2,X_test2,y_train2,y_test2 = train_test_split(X2,y2,test_size=0.2)

print(X_train2.shape)
print(X_test2.shape)
print(y_train2.shape)
print(y_test2.shape)


#KNN Algorithm - first try


import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics


data = pd.read_csv('D:\datas\excel\Day19\car_evaluation\car.data')
data.head()


X3 = data[[
    'buying','maint','safety'
]].values

y3 = data[['class']]

print(X3,y3)


#from sklearn.preprocessing import LabelEncoder

# conversion for X
le = LabelEncoder()
for i in range(len(X3[0])):
    X3[:,i] = le.fit_transform(X3[:,i])

print(X3)


# conversion for Y
label_mapping = {
    'unacc':0,
    'acc':1,
    'good':2,
   'vgood': 3
}
print(label_mapping)
y3['class']=y3['class'].map(label_mapping)
y3= np.array(y3)
print(y3)


#creation of KNN Model

knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2)

knn.fit(X_train3, y_train3)

y_pred = knn.predict(X_test3)

accuracy = metrics.accuracy_score(y_test3, y_pred)
print("Predictions: ", y_pred)
print("\nAccuracy: ", accuracy)


print("Actual Value : ",y3[20])
print("Predicted Value : ",knn.predict(X3)[20])


import matplotlib.pyplot as plt
import pandas as pd
X4 = pd.DataFrame(data.head(30))
y4 = pd.DataFrame(data.head(30))
X5=np.array(X4)
y5=np.array(y4)
plt.scatter(X5,y5)
plt.show()