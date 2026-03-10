class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Stack to keep track of opening brackets
        stack = []
        
        # Traverse each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the topmost element if the stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched
        return not stack
            