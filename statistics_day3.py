import pandas as pd
import random
import matplotlib.pyplot as plt


# for 2 dices
L=[]
for i in range(10000):
    a=random.randint(1,6)
    b=random.randint(1,6)
    L.append(a+b)



print(len(L))

print(L[:5])

s=(pd.Series(L).value_counts()/pd.Series(L).value_counts().sum()).sort_index()

print(s)

s.plot(kind='bar')
plt.show()


import numpy as np
print(np.cumsum(s))


np.cumsum(s).plot(kind='bar')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

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