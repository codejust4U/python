import math
 
def minimax (curDepth, nodeIndex,
             maxTurn, scores,
             targetDepth):
 
    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                    False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                     True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                     True, scores, targetDepth))
     
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]
 
treeDepth = math.log(len(scores), 2)
 
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
 
# This code is contributed
# by rootshadow

"""
import math

def minimax(current_depth, node_index, maxTurn, scores, target_depth):
    if current_depth == target_depth:
        return scores[node_index]
    
    if maxTurn:
        return max(
            minimax(current_depth + 1, node_index * 2, False, scores, target_depth),
            minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth)
        )
    else:
        return min(
            minimax(current_depth + 1, node_index * 2, True, scores, target_depth),
            minimax(current_depth + 1, node_index * 2 + 1, True, scores, target_depth)
        )

scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = int(math.log(len(scores), 2))

print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))

"""