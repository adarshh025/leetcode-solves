class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the top element if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the required opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to the stack
                stack.append(char)
                
        # If the stack is empty, all brackets are matched
        return not stack