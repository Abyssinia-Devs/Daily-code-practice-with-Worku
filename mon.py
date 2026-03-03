def minSwaps(grid):
    n = len(grid)
    
    #calculate trailing zeros for each row
    trailing_zeros = []
    for row in grid:
        count = 0
        for cell in reversed(row):
            if cell == 0:
                count += 1
            else:
                break
        trailing_zeros.append(count)
    
    #Perform swaps
    swaps = 0
    for i in range(n):
        required_zeros = n - i - 1
        
        # Find a row with enough trailing zeros
        j = i
        while j < n and trailing_zeros[j] < required_zeros:
            j += 1
        
        # If no such row exists
        if j == n:
            return -1
        
        # Bring that row up by swapping
        while j > i:
            trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
            swaps += 1
            j -= 1
    
    return swaps

# boom shakalaka tu!
n =[[0,0,1],[1,1,0],[1,0,0]]
            
        
print(minSwaps(n))
    
