class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split()
        count = 0
        
        for word in words:
            is_valid = True
            for char in word:
                if char in broken_set:
                    is_valid = False
                    break
            if is_valid:
                count += 1
                
        return count