class Solution:
    def findFinalValue(self, nums, original):
        condition = True
        
        while condition:
            for i in nums: # 5,3,6,1,12
                if i == original: #5!=3, 3=3 ,o=6,6=6, o=12,  1!=12, 12=12,o=224
                    original *= 2
            if not original in nums:
                condition =False
        return original
s1 = Solution()
nums = [5,3,6,1,12]
original = 3
nums = [2,7,9]
original = 4
nums = [8,1,16,4,2,9,32,5,1,2,3,5]
original = 2

print(s1.findFinalValue(nums, original))