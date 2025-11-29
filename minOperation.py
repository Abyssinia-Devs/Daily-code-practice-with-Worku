class Solution:
    def solve(self, num, k):
        return sum(num) % k

s1 = Solution()
print(s1.solve([1,2,3,4,5], 5))
