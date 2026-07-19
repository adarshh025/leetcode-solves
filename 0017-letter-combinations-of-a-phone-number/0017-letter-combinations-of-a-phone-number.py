from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # Map digits to their corresponding letters
        keypad = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_path: str):
            # Base case: if the path length equals digits length, we have a complete combination
            if index == len(digits):
                result.append(current_path)
                return
                
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = keypad[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, current_path + letter)
                
        # Start backtracking from index 0 with an empty string
        backtrack(0, "")
        
        return result