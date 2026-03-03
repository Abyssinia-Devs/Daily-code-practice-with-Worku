"""
give formula: Si = Si - 1 + "1" + reverse(invert(Si - 1))
this will be done by recursion formula
base case: S1 = "0"
Length(S_n) = 2^n - 1

# """
# def findKthBit(n, k):
#     # sn = n
#     # S_i = findKthBit(n-1, k) + "1" + reverse(invert(findKthBit(n-1, k)))
#     # len_sn = len(sn)
#     # if sn==1:
#     #     return 0
    
    
def findKthBit(n, k):
# Base case: If n == 1, the string is "0"
    if n == 1:
        return '0'

    # Length of S_n
    length = (2 ** n) - 1
    mid = (length // 2) + 1

    if k == mid:
        return '1'  # Middle bit is always '1'
    elif k < mid:
        return findKthBit(n - 1, k)  # Recur on the first half
    else:
        # Recur on the reversed and inverted second half
        # Find corresponding index in S_{n-1}
        corresponding_index = length - k + 1
        return '0' if findKthBit(n - 1, corresponding_index) == '1' else '1'
    
    
n = 4
k = 11
print(findKthBit(n, k))