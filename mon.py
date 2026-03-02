def minSwap(n):
    size = len(n)
    zeros_in_ith_row = []
    for i in range(len(n[0])):
        zeros_in_ith_row.append(n[i].count('0'))
    
    swap = 0
    for i in range(size):
        requered_zeros = (size - i - 1)
        j = i
        while j<size and zeros_in_ith_row[j] < requered_zeros:
            j+=1
        if j == size:
            return -1
        
        while j > i:
            zeros_in_ith_row[j], zeros_in_ith_row[j-1] = zeros_in_ith_row[j-1], zeros_in_ith_row[j]
            swap +=1
            j -=1
    return swap

n = [[1,0,0],[1,1,0],[1,1,1]]
            
        
    