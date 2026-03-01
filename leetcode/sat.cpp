class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        # LOOP 1: Pick the starting point(i)
        for i in range(n):
            #we need a clean slate for every new start position
            count = [0] * 26

            #LOOP 2: expand the window to the right(j)
            for j in range(i, n):
                # Calculate the correct index for the letter
                char_index = ord(s[j]) - ord('a')
                count[char_index] +=1

                #Reset our flag for this spcific substring
                is_balanced = True
                c_f = -1

                # Iterate through the frequencies directly
                for freq in count:
                    if freq == 0:
                        continue #Skip letters that arenot in substring(it is obvious)
                    if c_f == -1:
                        c_f = freq  # this is our target frequencey☺️🎉
                    elif freq !=c_f:
                        is_balanced = False
                        break #fail immediately 
                if is_balanced:
                    # update the longest substring
                    max_len = max(max_len, j - i + 1)
        return max_len

                    
print(Solution().longestBalanced("abbac")) 
