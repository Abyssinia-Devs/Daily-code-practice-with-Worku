class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        u = min([len(i) for i in strs])
        flag = False
        count = 0
        try:
            if strs[1] == "":
                return ""
        except:
            pass
        try:
            x = strs[1][0]
        except:
            return strs[0]
        for i in range(u):
            for j in range(len(strs)):
                x = (strs[j][i])
                if x in strs[0][i]:
                    continue
                else:
                    flag = True
                    break
            if flag:
                break
            count += 1
        if count >=1:
            return strs[0][:count]
        else:
            return ""
            
            
strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
# strs = [""]
s1 = Solution()

print(s1.longestCommonPrefix(strs))