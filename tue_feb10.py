class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        max_len = 0
        
        # Iterate over every possible starting point of the subarray
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            # Extend the subarray to the right
            for j in range(i, n):
                val = nums[j]
                
                # Add to appropriate set (set handles uniqueness automatically)
                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
                
                # Check condition
                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    max_len = max(max_len, current_len)
                    
        return max_len
