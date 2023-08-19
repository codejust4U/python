import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

iris = sns.load_dataset('iris')
print(iris)

# Axes level function
sns.stripplot(data=tips,x='day',y='total_bill')
plt.show()


# figure level
sns.catplot(data=tips,x='day',y='total_bill',kind='strip')
plt.show()

sns.catplot(data=tips,x='day',y='total_bill',kind='strip',jitter=0.15,hue='sex')
plt.show()

# Axes levle
sns.swarmplot(data=tips,x='day',y='total_bill')

plt.show()

sns.catplot(data=tips,x='day',y='total_bill',kind='swarm',hue='sex')
plt.show()


# Axes lvele
sns.boxplot(data=tips,x='sex',y='total_bill')
plt.show()


# fig level
sns.boxplot(data=tips,x='day',y='total_bill')
plt.show()

sns.boxplot(data=tips,x='day',y='total_bill',hue='sex')
plt.show()

sns.boxplot(data=tips,y='total_bill')
plt.show()

sns.violinplot(data=tips,x='day',y='total_bill')
plt.show()

sns.catplot(data=tips,x='day',y='total_bill',kind='violin')
plt.show()

sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex',split='True')
plt.show()

sns.barplot(data=tips,x='sex',y='total_bill',errorbar=None)
plt.show()

import numpy as np
sns.barplot(data=tips,x='sex',y='total_bill',hue='smoker',estimator=np.min,ci=None)
plt.show()


sns.pointplot(data=tips,x='sex',y='total_bill',hue='smoker',estimator='mean',errorbar=None)
plt.show()


sns.countplot(data=tips,x='sex',hue='day')
plt.show()

sns.catplot(data=tips,x='sex',y='total_bill')
plt.show()

sns.catplot(data=tips,x='sex',y='total_bill',col='smoker',row='time',kind='box')
plt.show()

# Axes 
# no hue parameter
sns.regplot(data=tips,x='total_bill',y='tip')
plt.show()

# Figure
sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex')
plt.show()

sns.residplot(data=tips,x='total_bill',y='tip')
plt.show()

# Fig level -> relplot -> displot -> catplot -> lmplot
sns.catplot(data=tips,x='sex',y='total_bill',kind='violin',col='day',row='time')
plt.show()

g=sns.FacetGrid(data=tips,col='day',row='time',hue='sex')
g.map(sns.violinplot,'sex','total_bill')
g.add_legend()
plt.show()

g=sns.FacetGrid(data=tips,col='day',row='time',hue='sex')
g.map(sns.scatterplot,'sex','total_bill')
g.add_legend()
plt.show()


print(iris)


sns.pairplot(iris)
plt.show()

sns.pairplot(iris,hue='species')
plt.show()


s=sns.PairGrid(data=iris,hue='species')
s.map(sns.scatterplot)
plt.show()

s2=sns.PairGrid(data=iris,hue='species')
s2.map_diag(sns.histplot)
s2.map_offdiag(sns.scatterplot)
s2.add_legend()
plt.show()


s2=sns.PairGrid(data=iris,hue='species')
s2.map_diag(sns.violinplot)
s2.map_offdiag(sns.scatterplot)
plt.show()


s2=sns.PairGrid(data=iris,hue='species')
s2.map_diag(sns.kdeplot)
s2.map_offdiag(sns.scatterplot)
s2.add_legend()
plt.show()

s2=sns.PairGrid(data=iris,hue='species')
s2.map_diag(sns.histplot)
s2.map_upper(sns.kdeplot)
s2.map_lower(sns.scatterplot)
# s2.add_legend()
plt.show()


s2=sns.PairGrid(data=iris,hue='species',vars=['sepal_length','petal_length'])
s2.map_diag(sns.histplot)
s2.map_upper(sns.kdeplot)
s2.map_lower(sns.scatterplot)
plt.show()

sns.jointplot(data=tips,x='total_bill',y='tip',kind='scatter')
plt.show()

sns.jointplot(data=tips,x='total_bill',y='tip',kind='kde')
plt.show()

sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist')
plt.show()

sns.jointplot(data=tips,x='total_bill',y='tip',kind='reg')
plt.show()

sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist',hue='sex')
plt.show()

g = sns.JointGrid(data=tips)
g.plot(sns.scatterplot,sns.histplot)
plt.show()

g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.scatterplot,sns.histplot)
plt.show()

g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.scatterplot,sns.kdeplot)
plt.show()


g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.scatterplot,sns.violinplot)
plt.show()

print(sns.get_dataset_names())

print(sns.load_dataset('flights'))