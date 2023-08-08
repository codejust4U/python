import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate samples from two normal distributions
sample1 = np.random.normal(loc=20, scale=5, size=300)
sample2 = np.random.normal(loc=40, scale=5, size=700)

# Combine the two samples into one array
sample = np.hstack((sample1, sample2))

print(sample)


plt.hist(sample,bins=50)
plt.show()


from sklearn.neighbors import KernelDensity

model = KernelDensity(bandwidth=3,kernel='gaussian')

#into 2D
sample=sample.reshape((len(sample),1))

model.fit(sample)

values = np.linspace(sample.min(),sample.max(),100)
values =values.reshape((len(values),1))

prob = model.score_samples(values)
prob = np.exp(prob)

plt.hist(sample, bins=50, density=True, alpha=0.6)
plt.plot(values, prob, label='KDE')
plt.title("Kernel Density Estimation")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

import seaborn as sns
sns.kdeplot(sample.reshape(1000),bw_adjust=1)

plt.show()



import seaborn as sns
df = sns.load_dataset('iris')
df.head()

sns.kdeplot(data=df,x='sepal_length',hue='species')
plt.show()

sns.kdeplot(data=df,x='sepal_width',hue='species')
plt.show()

sns.kdeplot(data=df,x='petal_length',hue='species')
plt.show()

sns.kdeplot(df['petal_length'])
plt.show()


dataset = pd.read_csv(r'D:\copy of htdocs\practice\Python\200days\Day126 EDA\Titanic-Dataset.csv')
dataset.head()

sns.kdeplot(data=dataset,x='Age',hue='Survived')
plt.show()


#sns.displot(data=df, x='petal_width', kind='ecdf', hue='species')
sns.kdeplot(data=df, x='petal_width', hue='species')
sns.ecdfplot(data=df, x='petal_width', hue='species')
plt.show()

sns.jointplot(data=df,x='petal_length',y='sepal_length',kind='kde',Fill=True,cbar=True,shade=True)
plt.show()


sns.jointplot(data=df, x='petal_length', y='sepal_length', kind='kde', shade=True, cmap='viridis', cbar=True)
plt.show()


