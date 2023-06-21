import numpy as np
import matplotlib.pyplot as plt

#no of cricket bat used in a split
n_cricket = np.array([3,5,7,9,11,13,17,19,21,23,24,25,32,35,37])
#no of balls used in a split
n_balls = np.array([1,3,7,8,8,11,17,22,23,24,27,28,29,36,38])
x1 = np.array([1,5,10,15,20,25,35,40])
y1 = np.array([1,5,10,15,20,25,35,40])
plt.figure(figsize=(12,8))
plt.xlabel("No of cricket bats used in a season",fontsize=15)
plt.ylabel("No of cricket balls used in a season",fontsize=15)
plt.scatter(n_cricket,n_balls,color='gold')
plt.plot(x1,y1)
plt.title("Cricket bat used vs Cricket balls used in a single season",fontname='Bradley Hand ITC',fontsize=25)

plt.show()

print("--------------------------------------------------")

import numpy as np
import matplotlib.pyplot as plt

#no of cricket bat used in a split
n_cricket = np.array([3,5,7,9,11,13,17,19,21,23,24,25,32,35,37])
#no of balls used in a split
n_balls = np.array([1,3,7,8,8,11,17,22,23,24,27,28,29,36,38])
x1 = np.array([0,5,10,15,20,25,20,30])
y1 = np.array([5,9,13,17,21,25,29,33])
plt.figure(figsize=(12,8))
plt.xlabel("No of cricket bats used in a season",fontsize=15)
plt.ylabel("No of cricket balls used in a season",fontsize=15)
#plt.scatter(n_cricket,n_balls,color='gold')
plt.plot(x1,y1)
plt.title("Cricket bat used vs Cricket balls used in a single season \n Positive Linear Regression",fontname='Bradley Hand ITC',fontsize=25)

plt.show()
print("--------------------------------------------------")

import numpy as np
import matplotlib.pyplot as plt
try:
    #no of cricket bat used in a split
    n_cricket = np.array([3,5,7,9,11,13,17,19,21,23,24,25,32,35,37])
    #no of balls used in a split
    n_balls = np.array([1,3,7,8,8,11,17,22,23,24,27,28,29,36,38])
    x1 = np.array([0,5,10,15,20,25,20,30])
    y1 = np.array([33,29,25,21,17,13,9,5])
    plt.figure(figsize=(12,8))
    plt.xlabel("No of cricket bats used in a season",fontsize=15)
    plt.ylabel("No of cricket balls used in a season",fontsize=15)
    #plt.scatter(n_cricket,n_balls,color='gold')
    plt.plot(x1,y1)
    plt.title("Cricket bat used vs Cricket balls used in a single season\n Negative Linear Regression",fontname='Bradley Hand ITC',fontsize=25)

    plt.show()
except:
    print("Error 404 not found!")


print("--------------------------------------------------")