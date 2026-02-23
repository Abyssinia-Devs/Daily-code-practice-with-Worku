
def hasAllCodes(self, s: str, k: int) -> bool:

        # Set to store unique substrings of length k
    seen = set()
    
    # Total number of binary codes of length k
    from math import pow
    required_count = pow(2, k) 
    
    # Sliding window to extract substrings
    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        seen.add(substring)
        # Early exit if we've already found all possible codes
        if len(seen) == required_count:
            return True
    
    # Check if we found all possible binary codes
    return len(seen) == required_count

        