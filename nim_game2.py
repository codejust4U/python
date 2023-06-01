"""import numpy as np

heap = []
n = int(input("Enter the number of heaps: "))
for i in range(1,n+1):
    heap_val = int(input("enter the values of heaps: "))
    heap.append(heap_val)
print("Heap values are: \n",heap)"""
"""
#Note there are only two players
sub_val = int(input("enter the values to be subtracted from heap: "))

heap_index = (int(input("enter the index from which heap you want to remove the stone: "))-1)

#new_val = heap[heap_index] - sub_val

heap[heap_index] =  heap[heap_index] - sub_val

print("The heap values after subtraction are: \n",heap)
"""
"""
if heap[0] == 0 and heap[1] ==0:
    print("The heap is empty")
    
elif heap[0] != 0  and heap[1] != 0:
    while heap[0]!=0 and heap[1]!=0:
        sub_val = int(input("enter the values to be subtracted from heap: "))

        heap_index = (int(input("enter the index from which heap you want to remove the stone: "))-1)

        #new_val = heap[heap_index] - sub_val

        heap[heap_index] =  heap[heap_index] - sub_val

        print("The heap values after subtraction are: \n",heap)

else:
    print("idk")
    
"""
"""
for i in heap:
    if i%2!=0:
        while heap[0]!=0 and heap[1]!=0:
            sub_val = int(input("enter the values to be subtracted from heap: "))

            heap_index = (int(input("enter the index from which heap you want to remove the stone: "))-1)

            #new_val = heap[heap_index] - sub_val

            heap[heap_index] =  heap[heap_index] - sub_val

            print("The heap values after subtraction are: \n",heap)
        print('Player 2 won')
    else:
        while heap[0]!=0 and heap[1]!=0:
            sub_val = int(input("enter the values to be subtracted from heap: "))

            heap_index = (int(input("enter the index from which heap you want to remove the stone: "))-1)

            #new_val = heap[heap_index] - sub_val

            heap[heap_index] =  heap[heap_index] - sub_val

            print("The heap values after subtraction are: \n",heap)
        print('Player 1 won')"""
"""
import numpy as np

heap = []
n = int(input("Enter the number of heaps: "))
for i in range(1, n+1):
    heap_val = int(input("Enter the values of heaps: "))
    heap.append(heap_val)
print("Heap values are: \n", heap)
for i in heap:
    if i % 2 != 0:
        while heap[0] != 0 and heap[1] != 0:
            sub_val = int(input("Enter the value to be subtracted from the heap: "))
            heap_index = int(input("Enter the index from which heap you want to remove the stone: ")) - 1
            heap[heap_index] -= sub_val
            print("The heap values after subtraction are: \n", heap)
        print('Player 2 won')
    else:
        while heap[0] != 0 and heap[1] != 0:
            sub_val = int(input("Enter the value to be subtracted from the heap: "))
            heap_index = int(input("Enter the index from which heap you want to remove the stone: ")) - 1
            heap[heap_index] -= sub_val
            print("The heap values after subtraction are: \n", heap)
        print('Player 1 won')
"""
"""
heap = []
n = int(input("Enter the number of heaps: "))
for i in range(1, n + 1):
  heap_val = int(input("Enter the values of heaps: "))
  heap.append(heap_val)
print("Heap values are: \n", heap, "\n")

while heap[0] != 0 and heap[1] != 0:
  for i in range(len(heap)):
    if i % 2 != 0:
      sub_val = int(input("Enter the number of stones to remove: "))
      heap_index = int(input("Enter the pile number: ")) - 1
      heap[heap_index] -= sub_val
      print("After the removal, the stones in heap are: \n", heap, "\n")
      if heap[0] == 0 or heap[1] == 0:
        print('Player 1 won')
        break
    else:
      sub_val = int(input("Enter the number of stones to remove: "))
      heap_index = int(input("Enter the pile number: ")) - 1
      heap[heap_index] -= sub_val
      print("After the removal, the stones in heap are: \n", heap, "\n")
      if heap[0] == 0 or heap[1] == 0:
        print('Player 2 won')
        break

"""

heap = []
n = int(input("Enter the number of heaps: "))
for i in range(1, n + 1):
  heap_val = int(input("Enter the values of heaps: "))
  heap.append(heap_val)
print("Heap values are: \n", heap, "\n")

match n:
  
  case 1:
    print("Can't be only one heap")
  case 2:
    while heap[0] != 0 and heap[1] != 0:
        for i in range(len(heap)):
                if i % 2 != 0:
                    sub_val = int(input("Enter the number of stones to remove: "))
                    heap_index = int(input("Enter the pile number: ")) - 1
                    heap[heap_index] -= sub_val
                    print("After the removal, the stones in heap are: \n", heap, "\n")
                    if heap[0] == 0 or heap[1] == 0:
                        print('Player 1 won')
                        break
                else:
                    sub_val = int(input("Enter the number of stones to remove: "))
                    heap_index = int(input("Enter the pile number: ")) - 1
                    heap[heap_index] -= sub_val
                    print("After the removal, the stones in heap are: \n", heap, "\n")
                    if heap[0] == 0 or heap[1] == 0:
                        print('Player 2 won')
                        break

  case 3:
     while heap[0] != 0 and heap[1] != 0 and heap[2] != 0:
        for i in range(len(heap)):
                if i % 2 != 0:
                    sub_val = int(input("Enter the number of stones to remove: "))
                    heap_index = int(input("Enter the pile number: ")) - 1
                    heap[heap_index] -= sub_val
                    print("After the removal, the stones in heap are: \n", heap, "\n")
                    if heap[0] == 0 or heap[1] == 0:
                        print('Player 1 won')
                        break
                else:
                    sub_val = int(input("Enter the number of stones to remove: "))
                    heap_index = int(input("Enter the pile number: ")) - 1
                    heap[heap_index] -= sub_val
                    print("After the removal, the stones in heap are: \n", heap, "\n")
                    if heap[0] == 0 or heap[1] == 0:
                        print('Player 2 won')
                        break
  case _:
    print("Invalid")
    