import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

url = 'https://raw.githubusercontent.com/codejust4U/dataset/main/maternal_health_risk.csv'
dataset = pd.read_csv(url)


dataset.head()

dataset.info()

dataset.describe().T

plot = sb.pairplot(dataset,hue='RiskLevel')

plot.fig.suptitle("Scatterplot and histogram of pairs of variables color coded by risk level",fontsize=14,y=1.05)

dataset['RiskLevel'].unique()

dataset['RiskLevel'] = dataset['RiskLevel'].replace('low risk',0).replace('mid risk',1).replace('high risk',2)

y = dataset['RiskLevel']
X = dataset.drop(['RiskLevel'], axis=1)

SEED = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)


rfc = RandomForestClassifier(n_estimators=3, 
                             max_depth=2,
                             random_state=SEED)



rfc.fit(X_train, y_train)

y_pred = rfc.predict(X_test)

features = X.columns.values
classes = ['0', '1', '2'] 

for estimator in rfc.estimators_:
    print(estimator)
    plt.figure(figsize=(12,6))
    tree.plot_tree(estimator,
                   feature_names=features,
                   class_names=classes,
                   fontsize=8, 
                   filled=True, 
                   rounded=True)
    plt.show()