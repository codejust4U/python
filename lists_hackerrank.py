"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""
  
  
  
  if __name__ == '__main__':
    N = int(input())
    L=[];
    for i in range(0,N):
        inp = input().split()
        if inp[0] == "insert":
            L.insert(int(inp[1]),int(inp[2]))
        elif inp[0] =="append":
            L.append(int(inp[1]))
        elif inp[0] == "pop":
            L.pop()
        elif inp[0] == "print":
            print(L)
        elif inp[0] == "remove":
            L.remove(int(inp[1]))
        elif inp[0] == "sort":
            L.sort()
        else:
            L.reverse()
            
    
