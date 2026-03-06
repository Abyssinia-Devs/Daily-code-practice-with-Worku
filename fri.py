class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if (s.count('1') == 0 or s.count('1')==1): return True
        c=0
        for i in range(len(s)-1):
            if s[i] == '1' and s[i+1] == '1' and s[i+1:].count('0') == len(s[i+2:]): return True
            if s[i]=='1' and s[i+1] == '0' and len(s[:i+1]) != len(s)-1: return False
        
        return True 
            
