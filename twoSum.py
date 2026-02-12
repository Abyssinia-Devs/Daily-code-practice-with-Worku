""" Begin
- Read a counter that increases its value in every iteration of the first loop.
- Loop through nums and store each value in num.
- Again, loop from counter to len(nums) and store the value as i.
- For each num in nums, add the value at index i, and store the value as result
-  compare the result and target number
- if true, then 
           we found the answer , so return the index of num and value of i
    else
       - After finishing the second loop, increment i so that we correctly shift the range counter to the next value.
End
"""
class Solution:
    def twoSum(self, nums: list[int], target):
        i =1
        for num in nums: 
            for  j in range(i, len(nums)): #1,2,3,4 ...
                result = num + nums[j]      # 1+ 2, 1+3, 1+4 ...
                if result == target: # 2,
                    return [nums.index(num), j]
            i +=1

c1 = Solution()
item1=[1,2,3,4]
tar=5
print(c1.twoSum(item1, tar))     
    