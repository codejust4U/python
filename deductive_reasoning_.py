"""data1 = "All star are big in size"
data2 = "Sun is star"
d1 = []
d2 = []

for i in range(len(data1)):
    for j in range(len(data2)):
        if data2[j] in data1:
            print(data2[j])
        else:
            print("Invalid")"""


"""
Note:
All copy are checked
Physics is the copy
"""
data1 = str(input("Enter the 1st premise: "))
data2 = str(input("Enter the 2nd premise: "))

for i in data2:
    try:
        if data2 in data1:
            print(data2)
            break
    except:
        print("unknown error")