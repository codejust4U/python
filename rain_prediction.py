
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

dataset = pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day125 simple project #4\weatherAUS.csv')

X = dataset.iloc[:, [1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]].values
y = dataset.iloc[:, -1].values

imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
X = imputer.fit_transform(X)

le1 = LabelEncoder()
X[:, 0] = le1.fit_transform(X[:, 0])

le2 = LabelEncoder()
X[:, 4] = le2.fit_transform(X[:, 4])

# Handle the problematic column with string value 'W'
column_with_w = 6  # Replace with the actual index of the column
le3 = LabelEncoder()
X[:, column_with_w] = le3.fit_transform(X[:, column_with_w])

le4 = LabelEncoder()
X[:, 7] = le4.fit_transform(X[:, 7])

le5 = LabelEncoder()
X[:, -1] = le5.fit_transform(X[:, -1])

le6 = LabelEncoder()
y = le6.fit_transform(y)

ss = StandardScaler()
X = ss.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

clf = RandomForestClassifier(n_estimators=100,random_state=0)
clf.fit(X_train,y_train)

clf.score(X_train,y_train)

y_pred = clf.predict(X_test)

y_pred = le6.inverse_transform(y_pred)

print(y_test)

y_test = le6.inverse_transform(y_test)

y_test = y_test.reshape(-1,1)
y_pred = y_pred.reshape(-1,1)

df =  np.concatenate((y_test,y_pred),axis=1)


dataframe = pd.DataFrame(df,columns=['Rain on Tomorrow','Predictin of Rain'])

y_test = y_test.astype(str)  # Convert y_test back to string
y_pred = y_pred.astype(str)  # Convert y_pred to string

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

accuracy_score(y_test,y_pred)