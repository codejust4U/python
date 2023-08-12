import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt



df = sns.load_dataset('iris')

sns.kdeplot(df['sepal_length'])
plt.show()


temp=sorted(df['sepal_length'].tolist())

y_quant = []
for i in range(1,101):
    y_quant.append(np.percentile(temp,i))


samples=np.random.normal(loc=0,scale=1,size=1000)

x_quant = []
for i in range(1,101):
    x_quant.append(np.percentile(samples,i))

sns.scatterplot(x=x_quant,y=y_quant)
plt.show()




## QQ'
fig = sm.qqplot(df['sepal_length'],line='45',fit=True)
plt.show()

X=np.random.uniform(low=0,high=1,size=1000)

plt.hist(X)
plt.show()

from scipy import stats 
params=stats.uniform.fit(X)
dist = stats.uniform(loc=params[0],scale=params[1])

fig = sm.qqplot(X,dist=dist,line='45')
plt.title('QQplot of uniform distribution with uniform fit')
plt.show()

alpha=3
xm = 1

x=np.linspace(0.1,10,1000)

y=alpha*(xm**alpha)/(x**(alpha+1))
plt.plot(x,y)
plt.show()


plt.plot(np.log(x),np.log(y))

plt.show()


alpha=2
xm=1

x = stats.pareto.rvs(b=alpha,scale=xm,size=1000)
plt.hist(x)

params=stats.pareto.fit(x,floc=0)
dist=stats.pareto(b=params[0],scale=params[2])
fig=sm.qqplot(x,dist=dist,line='45')
plt.title("QQplot woth pareto distribution with Pareto fit")
plt.show()


#DIistributions

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer

df=pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day152 Statistics_day_5\Titanic-Dataset.csv')

df['Age'].isnull().sum()

df['Age'].fillna(df['Age'].mean(),inplace=True)

X = df.drop('Survived', axis=1)  # Drop the target column ('Survived') to get all features
y = df['Survived']  # Target variable

# Alternatively, if you want to explicitly select columns 1 and 2:
# X = df.iloc[:, 1:3]
# y = df.iloc[:, 0]

# Fill missing values in the 'Age' column
X['Age'].fillna(X['Age'].mean(), inplace=True)

# Continue with the rest of your code (train/test split, plotting, etc.)


X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=42)

plt.figure(figsize=(14,4))
plt.subplot(121)
sns.distplot(df['Age'])
plt.title('Age')
plt.figure(figsize=(14,4))
plt.subplot(122)
stats.probplot(X_train['Age'],dist="norm",plot=plt)
plt.title('Age QQplot')
plt.show()


clf=LogisticRegression()
clf2 = DecisionTreeClassifier()

clf.fit(X_train,y_train)
clf2.fit(X_train,y_train)


y_pred=clf.predict(X_test)
y_pred2=clf2.predict(X_test)

print("Accuracy LR :",accuracy_score(y_test,y_pred))
print("Accuracy DTC :",accuracy_score(y_test,y_pred2))


import numpy as np
from sklearn.preprocessing import FunctionTransformer

# Assuming X_train and X_test are your datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 1: Separate numeric and non-numeric columns
numeric_cols = X_train.select_dtypes(include=np.number).columns
non_numeric_cols = X_train.select_dtypes(exclude=np.number).columns

# Step 2: Create and apply the transformer for numeric data
trf_numeric = FunctionTransformer(func=np.log1p)
X_train_transformed_numeric = trf_numeric.fit_transform(X_train[numeric_cols])
X_test_transformed_numeric = trf_numeric.transform(X_test[numeric_cols])

# Step 3: Handle non-numeric data (if needed, for example, using one-hot encoding)
# For example, using pandas get_dummies:
X_train_transformed_non_numeric = pd.get_dummies(X_train[non_numeric_cols])
X_test_transformed_non_numeric = pd.get_dummies(X_test[non_numeric_cols])

# Step 4: Concatenate the transformed numeric and non-numeric data
X_train_transformed = pd.concat([X_train_transformed_numeric, X_train_transformed_non_numeric], axis=1)
X_test_transformed = pd.concat([X_test_transformed_numeric, X_test_transformed_non_numeric], axis=1)




# Create the models and fit them to the data
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()

clf3.fit(X_train_transformed, y_train)
clf4.fit(X_train_transformed, y_train)

# Make predictions on the test set
y_pred3 = clf.predict(X_test_transformed)
y_pred4 = clf2.predict(X_test_transformed)

# Evaluate the models
print("Accuracy LR:",accuracy_score(y_test, y_pred3))
print("Accuracy DTC:",accuracy_score(y_test,y_pred4))




X_transformed = trf_numeric.fit_transform(X)
clf = LogisticRegression()
clf2 = DecisionTreeClassifier()

print("Lr :",cross_val_score(clf,X_train_transformed,y,scoring='accuracy',cv=10))
print("dt :",cross_val_score(clf2,X_train_transformed,y,scoring='accuracy',cv=10))



plt.figure(figsize=(14,4))
plt.subplot(121)
stats.probplot(X_train['Fare'],dist="norm",plot=plt)
plt.title('Fare before log')
plt.show()

plt.figure(figsize=(14,4))
plt.subplot(122)
stats.probplot(X_train_transformed['Fare'],dist="norm",plot=plt)
plt.title('Fare after plto')
plt.show()


plt.figure(figsize=(14,4))
plt.subplot(121)
stats.probplot(X_train['Age'],dist="norm",plot=plt)
plt.title('Age before log')
plt.show()

plt.figure(figsize=(14,4))
plt.subplot(122)
stats.probplot(X_train_transformed['Age'],dist="norm",plot=plt)
plt.title('Age after plto')
plt.show()


trf2 = ColumnTransformer([('log',FunctionTransformer(np.log1p),['Fare'])],remainder='passthrough')
X_train_transformed=trf2.fit_transform(X_train)
X_test_transform=trf2.transform(X_test)

clf = LogisticRegression()
clf1 = DecisionTreeClassifier()

clf.fit(X_train_transformed,y_train)
clf2.fit(X_train_transformed,y_train)

y_pred=clf.predict(X_test_transform)
y_pred1 = clf.predict(X_test_transform)
print("Lr :",accuracy_score(y_test,y_pred))
print("dt :",accuracy_score(y_test,y_pred1))



def ap_transform(transform):

    x1=df.iloc[:,3:6]
    y1=df.iloc[:,0]

    trf = ColumnTransformer([('log',FunctionTransformer(transform),['Fare'])],remainder='passthrough')
    x_trans = trf.fit_transform(x1)
    clf = LogisticRegression()
    print("Accuracy :",np.mean(cross_val_score(clf,x_trans,y1,scoring='accuracy',cv=10)))

    plt.figure(figsize=(14,4))

    plt.subplot(121)
    stats.probplot(x1['Fare'],dist='norm',plot=plt)
    plt.title("Fare before transform")

    plt.subplot(122)
    stats.probplot(x_trans[:,0],dist="norm",plot=plt)
    plt.title("Fare after transform")
    plt.show()


# for x
ap_transform(lambda x: x)

# for square
ap_transform(lambda x: x**2)

# for square root
ap_transform(lambda x: x**1/2)

# for reciprocal
ap_transform(lambda x: 1/(x+0.0000001))


from sklearn.preprocessing import PowerTransformer


df2=pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day152 Statistics_day_5\concrete_data.csv')
df2.head()


print(df2.describe())

X3=df2.drop(columns=['Strength'])
y3 = df2.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X3,y3,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression

lr2 = LinearRegression()
np.mean(cross_val_score(lr2,X3,y3,scoring='r2'))

for col in X_train.columns:
    plt.figure(figsize=(14,4))
    plt.subplot(121)
    sns.distplot(X_train[col])
    plt.title(col)

    plt.subplot(122)
    stats.probplot(X_train[col],dist="norm",plot=plt)
    plt.title(col)
    



from sklearn.preprocessing import PowerTransformer

# Instantiate the PowerTransformer
pt = PowerTransformer()

# Fit and transform the training data
X_train_transformed3 = pt.fit_transform(X_train+0.000001)

# Transform the test data
X_test_transform3 = pt.transform(X_test+0.000001)

pd.DataFrame({'cols':X_train.columns,'box_cox_lambdas':pt.lambdas_})



from sklearn.metrics import r2_score
lr2 = LinearRegression()
lr2.fit(X_train_transformed3,y_train)
y_pred3 = lr2.predict(X_test_transform3)

r2_score(y_test,y_pred3)


pt = PowerTransformer(method='box-cox')
X_train_transformed3 = pt.fit_transform(X3+0.000001)

lr3 = LinearRegression()
np.mean(cross_val_score(lr3,X_train_transformed3,y3,scoring='r2'))


# before and after
X_train_transformed3 = pd.DataFrame(X_train_transformed3,columns=X_train.columns)
for col in X_train_transformed3.columns:
    plt.figure(figsize=(14,4))
    plt.subplot(121)
    sns.distplot(X_train[col])
    plt.title(col)

    plt.subplot(122)
    sns.distplot(X_train_transformed3[col])
    plt.title(col)

    plt.show()


# apply Yeo-Johnson transform
pt1 = PowerTransformer()

X_train_transformed3_1 = pt1.fit_transform(X_train)
X_test_transform3_2 = pt1.transform(X_test)

lr3 = LinearRegression()
lr3.fit(X_train_transformed3_1,y_train)

y_pred5 = lr3.predict(X_test_transform3_2)
print(r2_score(y_test,y_pred5))

pd.DataFrame({'cols':X_train.columns,'Yeo_Johnson_lambdas':pt1.lambdas_})


pt1_2 = PowerTransformer()

X_transformed2 = pt1_2.fit_transform(X3)

lr4 = LinearRegression()
np.mean(cross_val_score(lr4,X_transformed2,y3,scoring='r2'))


X_train_transformed2 = pd.DataFrame(X_train_transformed3_1,columns=X_train.columns)



# before and after
for col in X_train_transformed2.columns:
    plt.figure(figsize=(14,4))
    plt.subplot(121)
    sns.distplot(X_train[col])
    plt.title(col)

    plt.subplot(122)
    sns.distplot(X_train_transformed2[col])
    plt.title(col)

    plt.show()

pd.DataFrame({'cols':X_train.columns,'box_cox_lambdas':pt.lambdas_,'Yeo-Johnson_lambdas':pt1.lambdas_})