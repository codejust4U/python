# plotting the sin wave in scattter form

import numpy as np
import matplotlib.pyplot as plt

data1_1 = np.arange(0, 10, 0.1)
data1_2 = np.sin(data1_1)
data1_3 = data1_2 * np.sin(data1_1)
data1_4 = data1_1 + data1_2

fig1 = plt.figure(figsize=(10, 7))
axis1 = fig1.add_subplot(111, projection='3d')

axis1.scatter(data1_1, data1_2, data1_3, c=data1_4, cmap='cool')
axis1.set_xlabel('X')
axis1.set_ylabel('Y')
axis1.set_zlabel('Z')

plt.show()


# 3D line graph with Sine Wave Signal

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig2 = plt.figure(figsize=(10,8))
axis2 = plt.axes(111,projection='3d')
data2_1 = np.linspace(0,20,1000)
data2_2 = np.sin(data2_1)
data2_3 = np.cos(data2_1)

axis2.plot3D(data2_1,data2_2,data2_3,'red')
axis2.view_init(45,180)
plt.show()

"""
# Visualizing Bubble sort using Python
Modules Needed
Matplotlib: Matplotlib is an amazing visualization library in Python for 2D plots of arrays. To install it type the below command in the terminal.

pip install matplotlib
 PyQt5: PyQt5 is cross-platform GUI toolkit, a set of python bindings for Qt v5. One can develop an interactive desktop application with so much ease because of the tools and simplicity provided by this library. To install it type the below command in the terminal.


pip install PyQt5==5.9.2
So, with that all set up, let’s get started with the actual coding. 
"""

# imports
import random
from matplotlib import pyplot as plt, animation
  
# helper methods
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
  
  
# algorithms
def bubblesort(A):
    swapped = True
      
    for i in range(len(A) - 1):
        if not swapped:
            return
        swapped = False
          
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A
  
  
def visualize():
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)
      
    # creates a generator object containing all 
    # the states of the array while performing 
    # sorting algorithm
    generator = bubblesort(A)
      
    # creates a figure and subsequent subplots
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
    bar_sub = ax.bar(range(len(A)), A, align="edge")
      
    # sets the maximum limit for the x-axis
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
      
    # helper function to update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
  
    # creating animation object for rendering the iteration
    anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=True,
        blit=False,
        interval=15,
        save_count=90000,
    )
      
    # for showing the animation on screen
    plt.show()
    plt.close()
  
  
if __name__ == "__main__":
    visualize()


#Another way-------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

amount = 15
list1 = np.random.randint(0, 20, amount)
x = np.arange(0, amount, 1)
n = len(list1)

for i in range(n):
    for j in range(0, n - i - 1):
        plt.bar(x, list1)
        
        for k in range(amount):
            plt.text(x[k], list1[k] + 0.5, str(list1[k]), ha='center', va='bottom')  # Add text on top of each bar
        
        plt.pause(0.01)
        plt.clf()

        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

plt.bar(x, list1)
for k in range(amount):
    plt.text(x[k], list1[k] + 0.5, str(list1[k]), ha='center', va='bottom')  # Add text on top of each bar

plt.show()


print("------------------------------------------------------------------------")

# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random
  
  
# function to recursively divide the arra
def mergesort(A, start, end):
    if end <= start:
        return
  
    mid = start + ((end - start + 1) // 2) - 1
      
    # yield from statements have been used to yield 
    # the array from the functions 
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
  
# function to merge the array
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1
  
    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1
  
    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1
  
    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1
  
    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A
  
# function to plot bars
def showGraph():
      
    # for random unique values
    n=20
    a=[i for i in range(1, n+1)]
    random.shuffle(a)
    datasetName='Random'
      
    # generator object returned by the function
    generator = mergesort(a, 0, len(a)-1)
    algoName='Merge Sort'
      
    # style of the chart
    plt.style.use('fivethirtyeight')
      
    # set colors of the bars
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                      (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                     (1.0, 0, 0)]
        }
    )
  
    fig, ax = plt.subplots()
      
    # bar container 
    bar_rects = ax.bar(range(len(a)), a, align="edge", 
                       color=color_map(data_normalizer(range(n))))
      
    # setting the limits of x and y axes
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1*len(a)))
    ax.set_title("ALGORITHM : "+algoName+"\n"+"DATA SET : "+datasetName, 
                 fontdict={'fontsize': 13, 'fontweight': 'medium', 
                           'color' : '#E4365D'})
      
    # the text to be shown on the upper left
    # indicating the number of iterations
    # transform indicates the position with 
    # relevance to the axes coordinates.
    text = ax.text(0.01, 0.95, "", transform=ax.transAxes, 
                   color="#E4365D")
    iteration = [0]
  
    def animate(A, rects, iteration):
        for rect, val in zip(rects, A):
              
            # setting the size of each bar equal 
            # to the value of the elements
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))
      
    # call animate function repeatedly
    anim = FuncAnimation(fig, func=animate,
        fargs=(bar_rects, iteration), frames=generator, interval=50,
        repeat=False)
    plt.show()
  
showGraph()

print("----------------------3D visualization Merge Sort--------------------")


# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random
 
# merge sort function to divide the array
def mergesort(A, start, end):
    if end <= start:
        return
 
    mid = start + ((end - start + 1) // 2) - 1
 
    # yield from statement is used to
    # yield the array from the merge function
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
 
# function to merge the array
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1
 
    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1
 
    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1
 
    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1
 
    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A
 
# function to plot bars
def showGraph():
 
    # for random unique values
    n = int(input("enter array size\n"))
    a = [i for i in range(1, n + 1)]
    random.shuffle(a)
    datasetName = 'Random'
 
    # generator object returned by the function
    generator = mergesort(a, 0, len(a)-1)
    algoName = 'Merge Sort'
 
    # style of the chart
    plt.style.use('fivethirtyeight')
 
    # set colors of the bars
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                      (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                     (1.0, 0, 0)]
        }
    )
 
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
 
    # z values and positions of the bars
    z = np.zeros(n)
    dx = np.ones(n)
    dy = np.ones(n)
    dz = [i for i in range(len(a))]
 
    # Poly3dCollection returned into variable rects
    rects = ax.bar3d(range(len(a)), a, z, dx, dy, dz,
                     color = color_map(data_normalizer(range(n))))
 
    # setting and x and y limits equal to the length of the array
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title("ALGORITHM : " + algoName + "\n" + "DATA SET : " +
                 datasetName, fontdict = {'fontsize' : 13,
                                          'fontweight' : 'medium',
                                          'color' : '#E4365D'})
 
    # text to plot on the chart
    text = ax.text2D(0.1, 0.95, "", horizontalalignment ='center',
                     verticalalignment ='center',
                     transform = ax.transAxes, color ="#E4365D")
    iteration = [0]
 
    # animation function to be repeatedly called
    def animate(A, rects, iteration):
 
        # to clear the bars from the Poly3DCollection object
        ax.collections.clear()
        ax.bar3d(range(len(a)), A, z, dx, dy, dz,
                 color = color_map(data_normalizer(range(n))))
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))
             
    # animate function is called here and the generator object is passed
    anim = FuncAnimation(fig, func = animate,
        fargs =(rects, iteration), frames = generator, interval = 50,
        repeat = False)
    plt.show()
 
showGraph()


print("------------------------------")

"""
# How to Make a Time Series Plot with Rolling Average in Python?

Time Series Plot is used to observe various trends in the dataset over a period of time. In such problems, the data is ordered by time and can fluctuate by the unit of time considered in the dataset (day, month, seconds, hours, etc.). When plotting the time series data, these fluctuations may prevent us to clearly gain insights about the peaks and troughs in the plot. So to clearly get value from the data, we use the rolling average concept to make the time series plot. 

The rolling average or moving average is the simple mean of the last ‘n’ values. It can help us in finding trends that would be otherwise hard to detect. Also, they can be used to determine long-term trends. You can simply calculate the rolling average by summing up the previous ‘n’ values and dividing them by ‘n’ itself. But for this, the first (n-1) values of the rolling average would be Nan.

In this article, we will learn how to make a time series plot with a rolling average in Python using Pandas and Seaborn libraries. Below is the syntax for computing rolling average using pandas.

Syntax: pandas.DataFrame.rolling(n).mean()


We will be using the ‘Daily Female Births Dataset’. This dataset describes the number of daily female births in California in 1959. There are 365 observations from 01-01-1959 to 31-12-1959. You can download the dataset from this link.
"""

import pandas as pd
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Fetching the sample data from the URL
url = 'https://github.com/codejust4U/dataset/raw/main/daily-total-female-births.csv'

try:
    data_fetch = pd.read_csv(url, delimiter=',', encoding='utf-8')
    print(data_fetch)
except pd.errors.ParserError as e:
    print('Error occurred while parsing the CSV file:', str(e))

#declaring the view area
plt.figure(figsize=(15,5))

#plotting the time series using seaborn lineplot
sb.lineplot(x='Date',
            y='Births',
            data=data_fetch,
            label='Daily Births')


year = [ '1959-01-01', '1959-02-01', '1959-03-01', '1959-04-01', 
       '1959-05-01', '1959-06-01', '1959-07-01', '1959-08-01',
       '1959-09-01', '1959-10-01', '1959-11-01', '1959-12-01']
  
month = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 
       'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
  
plt.xticks(year,month)
plt.ylabel('Female births')


"""
# Compute Rolling Average using pandas.DataFrame.rolling.mean().
"""

data_fetch['7day_rolling_avg']=data_fetch.Births.rolling(7).mean()

data_fetch.head(10)
plt.figure(figsize=(15,5))

#plotting
sb.lineplot(x='Date',y='Births',data=data_fetch,label='Daily Births')

sb.lineplot(x='Date',y='7day_rolling_avg',data=data_fetch,label='Rolling avg')



"""
# Plotting Various Sounds on Graphs using Python and Matplotlib

Approach 

Import matplotlib, Numpy, wave, and sys module.

Open the audio file using the wave.open() method.

Read all frames of the opened sound wave using readframes() function.

Store the frame rate in a variable using the getframrate() function.

Finally, plot the x-axis in seconds using frame rate.

Use the matplotlib.figure() function to plot the derived graph

Use labels as per the requirement.
"""
"""import numpy as np
import matplotlib.pyplot as plt
import wave
import sys

def v_path(path: str):
    # Fetching the data
    music_data = wave.open('D:\excel_datas\day9\sample_wav.wav', 'rb')

    # Reading the frames
    signal = music_data.readframes(-1)
    signal = np.frombuffer(signal, dtype='int16')

    # Getting the frame rate
    f_rate = music_data.getframerate()

    time = np.linspace(0, len(signal) / f_rate, num=len(signal))
    plt.figure(1)
    plt.plot(time, signal)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the audio file.")
        sys.exit(1)

    path = sys.argv[1]
    v_path(path)"""



"""
Plotting Simple Plot

We’ll be following the object-oriented method for plotting. The plot function takes two arguments that are X-axis values and Y-axis values plot. In this case, we will pass the ‘X’ variable which has ‘Dates’ and ‘Y’ variable which has ‘Daily Confirmed’ to plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 
import pandas as pd

covid_data = pd.read_csv(r'D:\excel_datas\day7\case_time_series (2).csv')


data1 = covid_data.iloc[61:, 1].values
data2 = covid_data.iloc[61:, 3].values
data3 = covid_data.iloc[61:, 5].values
data4 = covid_data.iloc[61:, 0].values

plt.plot(data4, data1)
plt.xlabel('Date')
plt.ylabel('Total Confirmed Cases')
plt.title('COVID-19 Daily Cases')

fig = plt.figure(figsize=(12,8))
ax = plt.axes(projection='3d')
ax.scatter3D(data1, data2, data3, cmap='viridis')
ax.set_xlabel('Total Confirmed Cases')
ax.set_ylabel('Total Recovered Cases')
ax.set_zlabel('Total Deceased Cases')
ax.set_title('COVID-19 Cases')

plt.show()

print("----------------------------------")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv(r'D:\excel_datas\day7\case_time_series (2).csv')
 
Y = data.iloc[61:,1].values
R = data.iloc[61:,3].values
D = data.iloc[61:,5].values
X = data.iloc[61:,0]
 
plt.figure(figsize=(25,8))
 
ax = plt.axes()
ax.grid(linewidth=0.4, color='#8f8f8f')
 
ax.set_facecolor("black")
ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
ax.set_ylabel('Number of Confirmed Cases\n',
              size=25,color='#4bb4f2')
 
ax.plot(X,Y,
        color='#1F77B4',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='#035E9B')



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv(r'D:\excel_datas\day7\case_time_series (2).csv')
 
Y = data.iloc[61:,1].values
R = data.iloc[61:,3].values
D = data.iloc[61:,5].values
X = data.iloc[61:,0]
 
plt.figure(figsize=(25,8))
 
ax = plt.axes()
ax.grid(linewidth=0.4, color='#8f8f8f')
 
ax.set_facecolor("black")
ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
ax.set_ylabel('Number of Confirmed Cases\n',
              size=25,color='#4bb4f2')
 
plt.xticks(rotation='vertical',size='20',color='white')
plt.yticks(size=20,color='white')
plt.tick_params(size=20,color='white')
 
for i,j in zip(X,Y):
    ax.annotate(str(j),xy=(i,j+100),color='white',size='13')
     
ax.annotate('Second Lockdown 15th April',
            xy=(15.2, 860),
            xytext=(19.9,500),
            color='white',
            size='25',
            arrowprops=dict(color='white',
                            linewidth=0.025))
 
plt.title("COVID-19 IN : Daily Confirmed\n",
          size=50,color='#28a9ff')
 
ax.plot(X,Y,
        color='#1F77B4',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='#035E9B')





data = pd.read_csv(r'D:\excel_datas\day7\district.csv')
data.head()
 
re=data.iloc[:30,5].values
de=data.iloc[:30,4].values
co=data.iloc[:30,3].values
x=list(data.iloc[:30,0])
 
plt.figure(figsize=(25,10))
ax=plt.axes()
 
ax.set_facecolor('black')
ax.grid(linewidth=0.4, color='#8f8f8f')
 
 
plt.xticks(rotation='vertical',
           size='20',
           color='white')#ticks of X
 
plt.yticks(size='20',color='white')
 
 
ax.set_xlabel('\nDistrict',size=25,
              color='#4bb4f2')
ax.set_ylabel('No. of cases\n',size=25,
              color='#4bb4f2')
 
 
plt.tick_params(size=20,color='white')
 
 
ax.set_title('District wise breakdown\n',
             size=50,color='#28a9ff')
 
plt.bar(x,co,label='re')
plt.bar(x,re,label='re',color='green')
plt.bar(x,de,label='re',color='red')

for i,j in zip(x,co):
    ax.annotate(str(int(j)),
                xy=(i,j+3),
                color='white',
                size='15')
 
plt.legend(['Confirmed','Recovered','Deceased'],
           fontsize=20)

