import numpy as np


n = int(input("Enter the number of items to be in the list: "))
alist = []
blist = []
clist = []
dlist = []
print("enter the values for a matrix")
for i in range(1, n):
    val_a = int(input())
    val = alist.append(val_a)

for i in range(1, n):
    val_b = int(input())
    val = blist.append(val_b)
print("enter the values for b matrix")
for i in range(1, n):
    val_c = int(input())
    val = clist.append(val_c)

for i in range(1, n):
    val_d = int(input())
    val = dlist.append(val_d)

a = np.array([alist, blist])

b = np.array([clist, dlist])


print(a)
print("Displaying the value of 1st matrix afteer adding 1 to it:\n",a+1)
print(b)
print("addition of two arrays:\n",a+b)
