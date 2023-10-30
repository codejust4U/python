# Outlier detection and removal using IQR - Feature Engineering - Day 11

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('placement.csv')

print(df.shape)

print(df.describe())

print(df.sample(5))

sns.distplot(df['cgpa'])
plt.show()

print(df['cgpa'].skew())

sns.distplot(df['placed'])
plt.show()

print(df['placed'].skew())

sns.distplot(df['placement_exam_marks'])
plt.show()

print(df['placement_exam_marks'].skew())

sns.boxplot(df['placement_exam_marks'])
plt.show()

# finding IQR

percentile25 = df['placement_exam_marks'].quantile(0.25)
percentile75 = df['placement_exam_marks'].quantile(0.75)

print(percentile25)
print(percentile75)

IQR = percentile75 - percentile25
print(IQR)

upperlimit = percentile75 +(1.5 * IQR)
lowerlimit = percentile25 -(1.5 * IQR)

print(upperlimit)

print(lowerlimit)

print(df[df['placement_exam_marks']>upperlimit])

print(df[df['placement_exam_marks']<lowerlimit])

df0=df[df['placement_exam_marks']<upperlimit]
print(df0.shape)

# Comparing

plt.figure(figsize=(16,8))
plt.subplot(2,2,1)
sns.distplot(df['placement_exam_marks'])

plt.subplot(2,2,2)
sns.boxplot(df['placement_exam_marks'])

plt.subplot(2,2,3)
sns.distplot(df0['placement_exam_marks'])

plt.subplot(2,2,4)
sns.boxplot(df0['placement_exam_marks'])

plt.show()

df0_cap = df.copy()

df0_cap['placement_exam_marks'] = np.where(
    df0_cap['placement_exam_marks'] > upperlimit,
    upperlimit,
    np.where(
        df0_cap['placement_exam_marks'] < lowerlimit,
        lowerlimit,
        df0_cap['placement_exam_marks']
    )
)

print(df0.shape)

# Comparing

plt.figure(figsize=(16,8))
plt.subplot(2,2,1)
sns.distplot(df['placement_exam_marks'])

plt.subplot(2,2,2)
sns.boxplot(df['placement_exam_marks'])

plt.subplot(2,2,3)
sns.distplot(df0_cap['placement_exam_marks'])

plt.subplot(2,2,4)
sns.boxplot(df0_cap['placement_exam_marks'])

plt.show()

