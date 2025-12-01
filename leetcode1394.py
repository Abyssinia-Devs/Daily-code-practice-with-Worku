class Solution:
    def findLucky(self, arr):
        return max(list(i for i in arr if arr.count(i)==i)) if len(list(i for i in arr if arr.count(i)==i)) != 0 else -1
    
s1 = Solution()
check = []
print(s1.findLucky(check))