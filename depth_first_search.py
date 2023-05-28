graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'F': ['J', 'K'],
    'H' : [],
    'I' : [],
    'E': [],
    'G': [],
    'J': [],
    'K': []
}

visited  = set()
def depth_first_search(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for successor_element in graph[node]:
            #print("Now the Successor element : ",successor_element)
            depth_first_search(visited,graph,successor_element)

node_name = str(input("Enter the node: "))
depth_first_search(visited,graph,node_name)
