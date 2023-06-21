import numpy as np
import pandas as pd
import sklearn as sl
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Fetching the cleaned data
data2 = pd.read_csv(r'D:\datas\excel\day10\final_data.csv')

# Remove the 'Date' column from the input data
X = data2.drop(['Date', 'PrecipitationSumInches'], axis=1)

Y = data2['PrecipitationSumInches']
Y = Y.values.reshape(-1, 1)

# Create the linear regression model
clf = LinearRegression()
clf.fit(X, Y)

# Inputting the sample random data
inp = np.array([[74], [60], [55], [67], [49], [43], [33], [45], [57], [29.68], [10], [7], [2], [0], [4], [31]])
inp = inp.reshape(1, -1)

# Predict the precipitation
print("Precipitation in inches for the user input:", clf.predict(inp))


day_no = 798
days = [i for i in range(Y.size)]
print('The precipatation graph')
plt.figure(figsize=(12,8))
axis = plt.axes()
axis.grid(linewidth=0.4, color='#8f8f8f')
axis.set_facecolor('black')
plt.plot(days,Y)
plt.scatter(days,Y,color='gold')
plt.scatter(days[day_no],Y[day_no])
plt.title("Precipitation Level")
plt.xlabel("Days")
plt.ylabel('Precipitation in inches')

#display the precipitation level  in inches
plt.show()



#filer data
x_f = X.filter(['TempAvgF','DewPointAvgF','HumidityAvgPercent','VisibilityHighMiles','WindAvgMPH','DewPointLowF'],axis=1)
for i in range(x_f.columns.size):
    #subplotting the datas
    plt.subplot(3,2,i+1)
    #plotting the datas in scatter form from 0 to 100
    
    plt.scatter(days,x_f[x_f.columns.values[i][:100]],color='lime',alpha=.2)
    plt.plot(days,x_f[x_f.columns.values[i][:100]],color='lime',alpha=.2)
    plt.scatter(days[day_no],x_f[x_f.columns.values[i]][day_no],color='red')
    plt.title(x_f.columns.values[i])

#plotting a graph to observe the different trends
plt.show()