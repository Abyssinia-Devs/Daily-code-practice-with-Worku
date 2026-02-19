class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        # Check all substrings
        for i in range(n):
            for j in range(i+1, n+1):
                substring = s[i:j]
                # Only consider substrings with even length
                if len(substring) % 2 == 0:
                    mid = len(substring) // 2
                    left, right = substring[:mid], substring[mid:]
                    # Check if left is all 0s and right all 1s OR left all 1s and right all 0s
                    if (all(c == '0' for c in left) and all(c == '1' for c in right)) or \
                    (all(c == '1' for c in left) and all(c == '0' for c in right)):
                        count += 1
        return count



        