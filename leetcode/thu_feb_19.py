class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Approach 1: Bitwise method (efficient)
        # -------------------------------------
        # Step 1: Shift n right by 1 bit and XOR with n.
        # Example: n = 5 (binary 101)
        #   n >> 1 = 2 (binary 010)
        #   n ^ (n >> 1) = 111 (all bits are 1)
        #
        # Step 2: If the result is all 1s, then (result & (result + 1)) == 0.
        # This works because numbers like 111... have the property that
        # adding 1 makes them 1000..., and ANDing them gives 0.
        
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
s1=Solution()