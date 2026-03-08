class Solution:
    def maxFreqSum(self, s: str) -> int:
        g = ['a', 'e', 'i', 'o', 'u']
        v = [s.count(i) for i in set(s) if i in g] or [0]
        c =[s.count(i) for i in set(s) if i not in g] or [0]
        maxv = max(v)
        maxc=max(c)
        return max(0,maxc+maxv)

s1 = Solution()
s = "aeiaeia"
print(s1.maxFreqSum(s))