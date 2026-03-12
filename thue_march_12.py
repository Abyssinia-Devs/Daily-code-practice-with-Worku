class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]
    
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = new_digits
        
        # Check if the final two digits are equal
        return digits[0] == digits[1]
    
    
#simple 
