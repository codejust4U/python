# Outlier using percentile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('weight-height.csv')

print(df.head())

print(df.shape)

print(df['Height'].describe())

sns.distplot(df['Height'])
plt.show()

sns.boxplot(df['Height'])
plt.show()

upperlimit = df['Height'].quantile(0.99)
print(upperlimit)

lowerlimit = df['Height'].quantile(0.01)
print(lowerlimit)

new_df=df[(df['Height']>= lowerlimit) & (df['Height']<= upperlimit)]

print(new_df['Height'].describe())

sns.distplot(new_df['Height'])
plt.show()

sns.boxplot(new_df['Height'])
plt.show()

print(new_df['Height'].skew())

# Outlier using percentile


# Capping --> Winsorization
df['Height'] = np.where(df['Height'] >= upperlimit,
        upperlimit,
        np.where(df['Height'] <= lowerlimit,
        lowerlimit,
        df['Height']))


print(df.shape)

print(df['Height'].describe())

sns.distplot(df['Height'])
plt.show()

sns.boxplot(df['Height'])
plt.show()

