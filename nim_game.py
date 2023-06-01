def solve(p, n):
    G = 0
    for i in range(n):
  
        # if pile size is odd 
        if (p[i] % 2 != 0): 
              
            # We XOR pile size+1
            G ^= (p[i] + 1) 
          
        # if pile size is even
        else: 
  
            # We XOR pile size-1
            G ^= (p[i] - 1) 
      
    return G
  
# Driver code
  
# Game with 3 piles
n = 3
  
# pile with different sizes
p = [27,18,18]
  
# Function to return result of game
res = solve(p, n)
  
if (res == 0): # if G is zero
    print("Player 2 wins")
      
else: # if G is non zero
    print("Player 1 wins")
