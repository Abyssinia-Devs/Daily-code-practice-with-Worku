class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        square = [(i+1)**2 for i in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                r = square[i] + square[j]
                if r in square:
                    count +=1
        return count*2
