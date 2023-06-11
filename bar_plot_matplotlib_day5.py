"""
Bar Plot in Matplotlib

A bar plot or bar chart is a graph that represents the category of data with rectangular bars with lengths and heights that is proportional to the values which they represent. The bar plots can be plotted horizontally or vertically. A bar chart describes the comparisons between the discrete categories. One of the axis of the plot represents the specific categories being compared, while the other axis represents the measured values corresponding to those categories.
 

Creating a bar plot
The matplotlib API in Python provides the bar() function which can be used in MATLAB style use or as an object-oriented API. The syntax of the bar() function to be used with the axes is as follows:-

plt.bar(x, height, width, bottom, align)
The function creates a bar plot bounded with a rectangle depending on the given parameters. Following is a simple example of the bar plot, which represents the number of students enrolled in different courses of an institute. 
"""
import numpy as np
import matplotlib.pyplot as plt

data = {'C':25, 'C++':35, 'Java':70,
		'Python':50,'.Net' : 50}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(courses, values, color ='maroon',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Skills i have in different languages")
plt.show()

"""

Bar Plot in Matplotlib

A bar plot or bar chart is a graph that represents the category of data with rectangular bars with lengths and heights that is proportional to the values which they represent. The bar plots can be plotted horizontally or vertically. A bar chart describes the comparisons between the discrete categories. One of the axis of the plot represents the specific categories being compared, while the other axis represents the measured values corresponding to those categories.
 

Creating a bar plot
The matplotlib API in Python provides the bar() function which can be used in MATLAB style use or as an object-oriented API. The syntax of the bar() function to be used with the axes is as follows:-

plt.bar(x, height, width, bottom, align)
The function creates a bar plot bounded with a rectangle depending on the given parameters. Following is a simple example of the bar plot, which represents the number of students enrolled in different courses of an institute. """
import numpy as np
import matplotlib.pyplot as plt

data = {'C':25, 'C++':35, 'Java':70,
		'Python':50,'.Net' : 50}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(courses, values, color ='maroon',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Skills i have in different languages")
plt.show()
"""
Here plt.bar(courses, values, color=’maroon’) is used to specify that the bar chart is to be plotted by using the courses column as the X-axis, and the values as the Y-axis. The color attribute is used to set the color of the bars(maroon in this case).plt.xlabel(“Courses offered”) and plt.ylabel(“students enrolled”) are used to label the corresponding axes.plt.title() is used to make a title for the graph.plt.show() is used to show the graph as output using the previous commands.
 

Customizing the bar plot"""

import pandas as pd
import matplotlib.pyplot as plt

print("-------------------------Selecting multi rows-------------------------")
data1 = pd.read_csv(r'D:\excel_datas\day4\nba.csv',index_col='Name')


Team = data1['Team']
Height = data1['Height']
fig2 = plt.figure(figsize=(10,7))

plt.bar(Team[0:10],Height[0:10])
plt.show()
"""
Multiple bar plots
Multiple bar plots are used when comparison among the data set is to be done when one variable is changing. We can easily convert it as a stacked area bar chart, where each subgroup is displayed by one on top of the others. It can be plotted by varying the thickness and position of the bars. Following bar plot shows the number of students passed in the engineering branch:"""
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25
fig = plt.subplots(figsize =(10, 7))

IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]

br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, IT, color ='r', width = barWidth,
		edgecolor ='grey', label ='IT')
plt.bar(br2, ECE, color ='g', width = barWidth,
		edgecolor ='grey', label ='ECE')
plt.bar(br3, CSE, color ='b', width = barWidth,
		edgecolor ='grey', label ='CSE')

plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
		['2015', '2016', '2017', '2018', '2019'])

plt.legend()
plt.show()
"""
Stacked bar plot
Stacked bar plots represent different groups on top of one another. The height of the bar depends on the resulting height of the combination of the results of the groups. It goes from the bottom to the value instead of going from zero to value. The following bar plot represents the contribution of boys and girls in the team."""
import numpy as np
import matplotlib.pyplot as plt

N = 5
 
boys = (20, 35, 30, 35, 27)
girls = (25, 32, 34, 20, 25)
boyStd = (2, 3, 4, 1, 2)
girlStd = (3, 5, 2, 3, 3)
ind = np.arange(N)  
width = 0.35 

fig3 = plt.subplots(figsize=(10,7))
plot3_1 = plt.bar(ind,boys,width,yerr=boyStd)
plot3_2 = plt.bar(ind,girls,width, bottom=boys,yerr=boyStd)
plt.title("Contribution by the teams")
plt.ylabel("Conribution")
plt.xticks(ind,('t1','T2','T3','T4','T5'))
plt.yticks(np.arange(0,81,10))
plt.legend((plot3_1[0],plot3_2[0]),('boys','girls'))
plt.show()
"""Draw a horizontal bar chart with Matplotlib

Matplotlib is the standard python library for creating visualizations in Python. Pyplot is a module of Matplotlib library which is used to plot graphs and charts and also make changes in them. In this article, we are going to see how to draw a horizontal bar chart with Matplotlib.

Creating a vertical bar chart
Approach:
""""""
Importing matplotlib.pyplot as plt
Creating list x for discrete values on x-axis
Creating list y  consisting only numeric data for discrete values on y-axis
Calling plt.bar() function with parameters x,y as plt.bar(x,y)
Setting x_label() and y_label()
Setting title() for our bar chart
Calling plt.show() for visualizing our chart"""
x4 = ['one','two','three','four','five']
y4 = [57,22,98,34,62]
plt.bar(x4,y4,color='red')
plt.xlabel("Name")
plt.ylabel("Price")
plt.title("Bar graph")
plt.show()
y4 = ['one','two','three','four','five']
x4 = [57,22,98,34,62]
plt.barh(y4,x4,color='red')
plt.ylabel("Name")
plt.xlabel("Price")
plt.title("Bar graph")
plt.show()
"""Create a stacked bar plot in Matplotlib

In this article, we will learn how to Create a stacked bar plot in Matplotlib. Let’s discuss some concepts:

Matplotlib is a tremendous visualization library in Python for 2D plots of arrays. Matplotlib may be a multi-platform data visualization library built on NumPy arrays and designed to figure with the broader SciPy stack.
A bar plot or bar graph may be a graph that represents the category of knowledge with rectangular bars with lengths and heights that’s proportional to the values which they represent. The bar plots are often plotted horizontally or vertically.
Stacked bar plots represent different groups on the highest of 1 another. The peak of the bar depends on the resulting height of the mixture of the results of the groups. It goes from rock bottom to the worth rather than going from zero to value.
Approach:

Import Library (Matplotlib)
Import / create data.
Plot the bars in the stack manner."""
x5 = ['A','B','C','D']
y5_1 = [25,35,45,55]
y5_2 = [35,25,55,45]
plt.bar(x5,y5_1,color='gold')
plt.bar(x5,y5_2,color='red',bottom=y5_2)
plt.show()

#(Stacked bar chart with more than 2 data)
import numpy as np
import matplotlib.pyplot as plt

x6 = ['A', 'B', 'C', 'D']
y6_1 = np.array([10, 20, 10, 30])
y6_2 = np.array([20, 25, 15, 25])
y6_3 = np.array([12, 15, 19, 6])
y6_4 = np.array([10, 29, 13, 19])

plt.bar(x6, y6_1, color='black')
plt.bar(x6, y6_2, color='blue', bottom=y6_1)
plt.bar(x6, y6_3, color='purple', bottom=y6_1+y6_2)
plt.bar(x6, y6_4, color='gold', bottom=y6_1+y6_2+y6_3)

plt.show()

"""Stacked Percentage Bar Plot In MatPlotLib

A Stacked Percentage Bar Chart is a simple bar chart in the stacked form with a percentage of each subgroup in a group. Stacked bar plots represent different groups on the top of one another. The height of the bar depends on the resulting height of the combination of the results of the groups. It goes from the bottom to the value instead of going from zero to value. A percent stacked bar chart is almost the same as a stacked barchart. Subgroups are displayed on top of each other, but data are normalized to make in a sort that the sum of every subgroup is the same as the total for each one. """
# importing packages
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_excel(r"D:\excel_datas\day6\hours.xlsx")

# view dataset
print(df)

# plot a Stacked Bar Chart using matplotlib
df.plot(
	x = 'Name',
	kind = 'barh',
	stacked = True,
	title = 'Stacked Bar Graph',
	mark_right = True)

#Add Percentage on subgroups of each group
# importing packages
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_excel(r"D:\excel_datas\day6\hours.xlsx")

# view dataset
print(df)

# plot a Stacked Bar Chart using matplotlib
df.plot(
	x = 'Name',
	kind = 'barh',
	stacked = True,
	title = 'Stacked Bar Graph',
	mark_right = True)

df_total = df['Studied']+df['Slept']+df['Other']
df_rel = df[df.columns[1:]].div(df_total,0)*100

for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:,1:].cumsum(1)[n],df[n],df_rel[n])):
        plt.text(cs-ab/2,i,str(np.round(pc,1))+'%',va='center',ha='center')
# importing packages
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_excel(r"D:\excel_datas\day6\hours.xlsx")

# view dataset
print(df)

# plot a Stacked Bar Chart using matplotlib
df.plot(
	x = 'Name',
	kind = 'barh',
	stacked = True,
	title = 'Stacked Bar Graph',
	mark_right = True)

df_total = df['Studied']+df['Slept']+df['Other']
df_rel = df[df.columns[1:]].div(df_total,0)*100

for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:,1:].cumsum(1)[n],df[n],df_rel[n])):
        plt.text(cs-ab/2,i,str(np.round(pc,1))+'%',va='center',ha='center',rotation=45,color='white')
        
"""
Plotting back-to-back bar charts Matplotlib

In this article, we will learn how to plot back-to-back bar charts in matplotlib in python. Let’s discuss some concepts :

Matplotlib: Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was introduced by John Hunter in the year 2002.

Bar chart:  Bar plot or Bar chart is a graph that represents the category of data with rectangular bars with lengths and heights that is proportional to the values which they represent. The bar plots can be plotted horizontally or vertically.

Back-to-Back Bar Chart: Back-to-Back Bar Chart is just a combination of two bar charts drawn with respect to a axis.


Steps Needed
Import library (matplotlib)
Import / Load / Create data
Plot the Back-to-Back Bar Chart over data.
Here, we discuss some examples step by step to understand the concept in a better way.
import packages"""
import numpy as np
import matplotlib.pyplot as plt

# create data
A = np.array([3,6,9,4,2,5])
X = np.arange(6)

# plot the bars
plt.bar(X, A, color = 'r')
plt.bar(X, -A, color = 'b')
plt.title("Back-to-Back Bar Chart")
plt.show()

# import packages
import numpy as np
import matplotlib.pyplot as plt

# create data
A = np.array([3,6,9,4,2,5])
X = np.arange(6)

# plot the bars
plt.barh(X, A, color = 'r')
plt.barh(X, -A, color = 'b')
plt.title("Back-to-Back Bar Chart")
plt.show()

# import packages
import numpy as np
import matplotlib.pyplot as plt

# create data
A = np.array([3, 6, 9, 4, 2, 5])
B = np.array([5, 8, 3, 9, 3, 6])
X = np.arange(6)

# plot the bars
plt.barh(X, A, align='center', alpha=0.7, color='g')
plt.barh(X, -B, align='center', alpha=0.5, color='purple')
plt.title("Back-to-Back Bar Chart")
plt.show()
"""How to display the value of each bar in a bar chart using Matplotlib?

In this article, we are going to see how to display the value of each bar in a bar chart using Matplotlib. There are two different ways to display the values of each bar in a bar chart in matplotlib –

Using matplotlib.axes.Axes.text() function.
Use matplotlib.pyplot.text() function.
Example 1: Using matplotlib.axes.Axes.text() function:

This function is basically used to add some text to the location in the chart. This function return string, this is always used with the syntax “for index, value in enumerate(iterable)” with iterable as the list of bar values to access each index, value pair in iterable so at it can add the text at each bar."""


import os
import matplotlib.pyplot as plt
import numpy as np

x10 = [0, 1, 2, 3, 4, 5, 6, 7]
y10 = [160, 167, 17, 130, 120, 40, 105, 70]
fig10,axis10 = plt.subplots()
width = 0.75
ind = np.arange(len(y10))

axis10.barh(ind, y10, width, color='gold')
for i,v in enumerate(y10):
    axis10.text(v+3,i+.25,str(v),color='red',fontweight='bold')

plt.show()

"""Use matplotlib.pyplot.text() function:

Call matplotlib.pyplot.barh(x, height) with x as a list of bar names and height as a list of bar values to create a bar chart. Use the syntax “for index, value in enumerate(iterable)” with iterable as the list of bar values to access each index, value pair in iterable. At each iteration, call matplotlib.pyplot.text(x, y, s) with x as value, y as index, and s as str(value) to label each bar with its size."""
import matplotlib.pyplot as plt
x11 = ["A", "B", "C", "D"]
y11 = [1, 2, 3, 4]
plt.barh(x11,y11,color='purple',alpha=0.6)
for index, value in enumerate(y11):
    plt.text(value, index, str(value))

plt.show()
"""How To Annotate Bars in Barplot with Matplotlib in Python?

Annotation means adding notes to a diagram stating what values do it represents. It often gets tiresome for the user to read the values from the graph when the graph is scaled down or is overly populated.  In this article, we will discuss how to annotate the bar plots created in python using matplotlib library."""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data12 = {"Name": ["Alex", "Bob", "Clarein", "Dexter"],
        "Marks": [45, 23, 78, 65]}
df12 = pd.DataFrame(data12)

"""
Let’s now start plotting the dataframe using the seaborn library. We get the following results. But it is not quite visible that what are the actual values in the bar plots. This condition can also arise when the values of neighboring plots are quite close to each other."""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data12 = {"Name": ["Alex", "Bob", "Clarein", "Dexter"],
        "Marks": [45, 23, 78, 65]}
df12 = pd.DataFrame(data12)


plt.figure(figsize=(8,6))
plots12 = sns.barplot(x='Name',y='Marks',data=df12)
plt.xlabel("Students",size=15)
plt.ylabel("Secured marks",size=15)
plt.show()
"""Adding the annotations. Our strategy here will be to iterate all over the bars and put a text over all of them that will point out the values of that particular bar. Here we will use the Matlpotlib’s function called annotate(). We can find various uses of this function in various scenarios, currently, we will be just showing the value of the respective bars at their top.
Our steps will be:

Iterate over the bars
Get the x-axis position(x) and the width(w) of the bar this will help us to get the x coordinate of the text i.e. get_x()+get_width()/2.
The y-coordinate(y) of the text can be found using the height of the bar i.e. get_height()
So we have the coordinates of the annotation value i.e. get_x()+get_width()/2, get_height()
But this will print the annotation exactly on the boundary of the bar so to get a more pleasing annotated plot we use the parameter xyplot=(0, 8). Here 8 denotes the pixels that will be left from the top of the bar. Therefore to go below the barline we can use xy=(0,-8).
So we execute the following code to get the annotated graph:"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data12 = {"Name": ["Alex", "Bob", "Clarein", "Dexter"],
          "Marks": [45, 23, 76, 65]}
df12 = pd.DataFrame(data12)

plt.figure(figsize=(8, 6))
plots12 = sns.barplot(x='Name', y='Marks', data=df12)
for bar in plots12.patches:
    plots12.annotate(format(bar.get_height(), '.2f'), (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     ha='center', va='center', size=10, xytext=(0, 8), textcoords='offset points')

plt.xlabel("Students", size=14)
plt.ylabel("Secured marks", size=14)
plt.title('students vs secure marks graph')
plt.show()
"""
How to Annotate Bars in Grouped Barplot in Python?

A Barplot is a graph that represents the relationship between a categoric and a numeric feature. Many rectangular bars correspond to each category of the categoric feature and the size of these bars represents the corresponding value. Using grouped bar plots,  we can study the relationship between more than two features.

In Python, we can plot a barplot either using the Matplotlib library or using the seaborn library, which is a higher-level library built on Matplotlib and it also supports pandas data structures. In this article, we have used seaborn.barplot() function to plot the grouped bar plots.

Another important aspect of data visualization using bar plots is, using annotations i.e adding text for a better understanding of the chart. This can be achieved by using the annotate() function in pyplot module of matplotlib library as explained in the below steps.

Step 1: Importing the libraries and the dataset used. Here we have used the Titanic dataset, which is inbuilt with seaborn. """


# importing the libraries used
import seaborn as sns
import matplotlib.pyplot as plt

# Importing the dataset
df = sns.load_dataset("titanic")
print(df.head())

# transforming the dataset for barplot
data_df = df.groupby(['sex', 'class']).agg(
	avg_age=('age', 'mean'), count=('sex', 'count'))

data_df = data_df.reset_index()
print(data_df.head())

"""Explanation: Grouped bar plots require at least two categorical features and a numerical feature. Here, we have filtered out the ‘class’ feature to categorize and the ‘sex’ feature to group the bars using pandas.Dataframe.groupby() function. Then we have aggregated the mean age and count for each group using pandas.core.groupby.DataFrameGroupBy.agg(). Previous operations resulted in a multi-index dataframe, hence we reset the index to obtain the dataset shown below.

Step 3: Now, we plot a simple Barplot using the transformed dataset using seaborn.barplot() function. """
# code to plot a simple grouped barplot
plt.figure(figsize=(8, 6))
sns.barplot(x="class", y="avg_age",
			hue="sex", data=data_df,
			palette='Greens')

plt.ylabel("Average Age", size=14)
plt.xlabel("Ticket Class", size=14)
plt.title("Simple Grouped Barplot", size=18)

plt.figure(figsize=(8,6))
splot=sns.barplot(x='class',y='avg_age',hue='sex',data=data_df,palette='Greens')

for p in splot.patches:
    splot.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',va='center',xytext=(0,9),textcoords='offset points')

plt.ylabel('Agerage age')
plt.xlabel('Ticket class')
plt.title("Age vs ticket class")
"""Explanation: In the above code, we have used the ‘patches’ attribute of the seaborn plot object to iterate over each bar. We have calculated the height, coordinates, and put text using the annotate function for each bar.

Step 5: Since each bar represents age and putting decimal doesn’t make its value sensible. We will customize our text by rounding off to the nearest integer and then using the format() function as shown in the code below."""
# code for annotated barplot
plt.figure(figsize=(8, 6))
splot = sns.barplot(x="class", y="avg_age", hue="sex",
					data=data_df, palette='Greens')

plt.ylabel("Average Age", size=14)
plt.xlabel("Ticket Class", size=14)
plt.title("Grouped Barplot with annotations", size=18)
for p in splot.patches:
	splot.annotate(format(round(p.get_height()), '.0f')+"Years",
				(p.get_x() + p.get_width() / 2., p.get_height()),
				ha='center', va='center',
				size=14,
				xytext=(0, -12),
				textcoords='offset points')

