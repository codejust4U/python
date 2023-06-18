"""# importing libraries  
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  
  
#importing datasets  
data_set= pd.read_csv('user_data.csv')  
  
#Extracting Independent and dependent Variable  
x= data_set.iloc[:, [2,3]].values  
y= data_set.iloc[:, 4].values  
  
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)  
  
#feature Scaling  
from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()  
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)    """

# Import the necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from graphviz import Source

# Load the dataset
iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target

# DecisionTreeClassifier
tree_clf = DecisionTreeClassifier(criterion='entropy',
								max_depth=2)
tree_clf.fit(X, y)

# Plot the decision tree graph
export_graphviz(
	tree_clf,
	out_file="iris_tree.dot",
	feature_names=iris.feature_names[2:],
	class_names=iris.target_names,
	rounded=True,
	filled=True
)

with open("iris_tree.dot") as f:
	dot_graph = f.read()
	
Source(dot_graph)
