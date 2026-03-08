from math import sqrt

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        
        total = 0
        while left <= right:
            left_1s = bin(left)[2:].count('1')
            if left_1s < 2:
                left +=1
                continue
            is_odd = True
            sq = int(sqrt(left_1s))+1
            for j in range(2, sq):
                if left_1s % j ==0:
                    is_odd = False
                    break
            
            if is_odd:
                total +=1

            left +=1


        return total
    