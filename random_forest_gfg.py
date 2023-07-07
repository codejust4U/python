import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

iris = datasets.load_iris()

print("Target names are : ",iris.target_names)

print("Feature names are : ",iris.feature_names)


X,y = datasets.load_iris(return_X_y=True)

X_train, X_test,y_train, y_test =  train_test_split(X,y,test_size=0.30)

data = pd.DataFrame({'sepallength': iris.data[:, 0], 'sepalwidth': iris.data[:, 1],
                     'petallength': iris.data[:, 2], 'petalwidth': iris.data[:, 3],
                     'species': iris.target})

print('\n\n',data.head(10))

clf = RandomForestClassifier(n_estimators=100)

clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print('\n\n',"Accuracy : ",(metrics.accuracy_score(y_test,y_pred))*100,"%")

predicted_val = clf.predict([[3,3,3,3]])
if predicted_val == [0]:
    print('\n\n',"Sepal Length",predicted_val)
elif predicted_val == [1]:
    print('\n\n',"Sepal Width",predicted_val)
elif predicted_val == [2]:
    print('\n\n',"Petal Length",predicted_val)
else:
    print('\n\n',"Petal Width",predicted_val)


feature_imp = pd.Series(clf.feature_importances_, index = iris.feature_names).sort_values(ascending = False)
print('\n\n',feature_imp)