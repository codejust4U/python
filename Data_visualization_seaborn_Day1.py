import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)


# Scatter plot
# axis level plot
sns.scatterplot(data=tips,x='total_bill',y='tip')
plt.show()


# using hue on above code and style , size
sns.scatterplot(data=tips,x='total_bill',y='tip',hue='sex',style='time',size='size')
plt.show()

# figure level plot
sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',hue='sex')
plt.show()


gap = px.data.gapminder()
print(gap)

temp_df=gap[gap['country']=='India']
print(temp_df)


sns.lineplot(data=temp_df,x='year',y='lifeExp')
plt.show()

sns.relplot(data=temp_df,x='year',y='lifeExp',kind='line')
plt.show()


t_df = gap[gap['country'].isin(['India','Pakistan','China'])]
print(t_df)


# Figure Level
sns.relplot(data=t_df,x='year',y='lifeExp',kind='line',hue='country')
plt.show()

# Axis Level
sns.lineplot(data=t_df,x='year',y='lifeExp',hue='country')
plt.show()

t_df2 = gap[gap['country'].isin(['Nepal','Germany','Iraq','Brazil'])]
print(t_df2)

sns.relplot(kind='line',data=t_df2,x='year',y='lifeExp',hue='country',style='continent',size='continent')
plt.show()

# ususal but can be replaced with below graph for better understanding
sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',hue='sex')
plt.show()

sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',col='sex')
plt.show()




sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',row='sex')
plt.show()


sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',col='sex',row='smoker')
plt.show()

sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',col='sex',row='day')
plt.show()

sns.relplot(data=tips,x='total_bill',y='tip',kind='line',col='sex',row='day')
plt.show()

# Column Wrap
sns.relplot(data=gap,x='lifeExp',y='gdpPercap',kind='scatter',col='year',col_wrap=4)
plt.show()


# univaraite histogram
sns.histplot(data=tips,x='total_bill')
plt.show()

sns.displot(data=tips,x='total_bill',kind='hist')
plt.show()



sns.displot(data=tips,x='total_bill',kind='hist',bins=20)
plt.show()

print(tips)

# acting like a countplot
sns.displot(data=tips,x='day',kind='hist')
plt.show()

sns.displot(data=tips,x='tip',hue='sex',kind='hist')
plt.show()

sns.displot(data=tips,x='tip',hue='sex',kind='hist',element='step')

plt.show()

titanic=sns.load_dataset('titanic')
print(titanic)


sns.displot(data=titanic,x='age',element='step',hue='sex')
plt.show()


sns.displot(data=tips,x='tip',element='step',kind='hist',col='sex')
plt.show()

print(tips)

sns.kdeplot(data=tips,x='total_bill')
plt.show()

sns.displot(data=tips,x='total_bill',kind='kde',hue='sex',fill=True)
plt.show()

sns.kdeplot(data=tips,x='total_bill')
sns.rugplot(data=tips,x='total_bill')
plt.show()

# for bivariate 
#sns.histplot(data=tips,x='total_bill',y='tip')
sns.displot(data=tips,x='total_bill',y='tip',kind='hist')

plt.show()

sns.kdeplot(data=tips,x='total_bill',y='tip')
plt.show()

t_df3 = gap.pivot(index='country',columns='year',values='lifeExp')
plt.show()

# axes level function
plt.figure(figsize=(15,15))
sns.heatmap(t_df3,cmap='winter')
plt.show()

# for one continent
t_df4=gap[gap['continent']=='Europe'].pivot(index='country',columns='year',values='lifeExp')

# axes level function
plt.figure(figsize=(15,15))
sns.heatmap(t_df4,annot=True,linewidths=0.5,cmap='viridis')
plt.show()

iris = sns.load_dataset('iris')
print(iris)

sns.clustermap(iris.iloc[:,[0,1,2,3]],cmap='viridis')
plt.show()


sns.displot(data=tips,x='total_bill',kind='kde',hue='sex',fill='True',height=10,aspect=1.5)
plt.show()
