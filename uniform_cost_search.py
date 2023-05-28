from queue import PriorityQueue

class Problem:
    def __init__(self):
        self.graph = {
            'A': [('B', 1), ('C', 2)],
            'B': [('D', 3), ('E', 4)],
            'C': [('F', 2), ('G', 3)],
            'D': [('H', 1), ('I', 2)],
            'E': [],
            'F': [('J', 3), ('K', 2)],
            'G': [],
            'H': [],
            'I': [],
            'J': [],
            'K': []
        }

    def getStartState(self):
        return 'A'

    def isGoalState(self, state):
        return state == 'E'

    def getSuccessors(self, state):
        return self.graph[state]

    def getCostOfActions(self, actions):
        cost = 0
        for action in actions:
            cost += action  # Accumulate the cost of each action
        return cost



def ucs(problem):
    successor_element = PriorityQueue()
    fringe = []
    path = []
    visited = set([])
    priority = 0
    dict = {}
    start_node = problem.getStartState()
    if problem.isGoalState(start_node):
        return "Already in goal"
    else:
        successor_element.put((start_node, path), priority)
        dict[start_node] = 0
        visited.add(start_node)
        while not successor_element.empty():
            curr, path = successor_element.get()
            if problem.isGoalState(curr):
                return path
            else:
                next = problem.getSuccessors(curr)
                for node in successor_element.queue:
                    fringe.append(node[0])

                for states in next:
                    if states[0] not in dict or problem.getCostOfActions(path + [states[1]]) < dict[states[0]]:
                        cost = problem.getCostOfActions(path + [states[1]])
                        successor_element.put((states[0], path + [states[1]]), cost)
                        dict[states[0]] = cost
                        visited.add(states[0])




problem = Problem()
list1 = ucs(problem)
print(list1)


cost1 = 0
for ele in range(0, len(list1)):
    cost1 = cost1 + list1[ele]
 
print("Minimum cost : ", cost1)
