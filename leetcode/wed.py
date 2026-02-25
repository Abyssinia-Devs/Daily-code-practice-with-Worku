class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sort = sorted([(bin(x).count('1'),x) for x in  (arr)])
        result = [x[1] for x in sort]
        return result