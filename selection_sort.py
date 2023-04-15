alist = []
n=int(input("Enter the size of numbers in list: ")) 
for i in range(0,n):
    a=int(input("enter the numbers : ")) 
    alist.append(a)
print("list of items is", alist)
def selectionSort(alist):
    for i in range(len(alist)-1,0,-1): 
        pos=0
        for location in range(1,i+1): 
            if alist[location]>alist[pos]:
                pos= location 
        temp = alist[i] 
        alist[i] = alist[pos] 
        alist[pos] = temp

selectionSort(alist) 
print("Sorted list items thorugh selection sort is",alist)
