import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_excel(r'D:\copy of htdocs\practice\Python\200days\Day148 Statistics-Day2\data.xlsx')
print(df)


plt.plot(df)
plt.show()


df['data'].plot(kind='box')
plt.show()
df['data'].plot(kind='hist')
plt.show()


df2=pd.read_excel(r'D:\copy of htdocs\practice\Python\200days\Day148 Statistics-Day2\data2.xlsx')
print(df2)


plt.scatter(df2['Price(in Lakhs)'],df2['House (in sq. ft)'],color='green')
plt.plot(df2['Price(in Lakhs)'],df2['House (in sq. ft)'],color='red')
plt.show()

df3=pd.read_excel(r'D:\copy of htdocs\practice\Python\200days\Day148 Statistics-Day2\covariance_data.xlsx')
print(df3)

import numpy as np



fig, (ax1,ax2) =plt.subplots(1,2,figsize=(10,3))
ax1.scatter(df3['X'],df3['Y'])
ax2.scatter(df3['X'],df3['X'],color='purple')
ax1.set_title("Covariance = "+str(np.cov(df3['X'],df3['Y'])[0,1]))
ax2.set_title("Covariance = "+str(np.cov(df3['X'],df3['X'])[0,1]))
plt.show()

df4=pd.read_excel(r'D:\copy of htdocs\practice\Python\200days\Day148 Statistics-Day2\neg_covariance.xlsx')
print(df4)




plt.scatter(df4['X'],df4['Y'])
fig, (ax1,ax2) =plt.subplots(1,2,figsize=(10,3))
ax1.scatter(df3['X'],df3['Y'])
ax2.scatter(df3['X']*2,df3['Y'])
ax1.set_title("Correlation : "+str(df3['X'].corr(df3['Y'])))
ax2.set_title("Correlation : "+str((df3['X']*2).corr(df3['Y']*2)))


plt.show()




