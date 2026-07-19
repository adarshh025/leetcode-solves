class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Dictionary to store the last index of each character
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, c in enumerate(s):
            # If the character is already in our result stack, skip it
            if c in seen:
                continue
                
            # While stack is not empty, top character is greater than current,
            # and the top character will appear again later in the string
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add current character to stack and mark as seen
            stack.append(c)
            seen.add(c)
            
        return "".join(stack)