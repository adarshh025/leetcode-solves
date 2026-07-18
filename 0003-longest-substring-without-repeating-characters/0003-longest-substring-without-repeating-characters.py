class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            # If char is seen and is inside the current window, move the left pointer
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            # Update the character's last seen index
            char_index[char] = right
            
            # Calculate the max length
            max_length = max(max_length, right - left + 1)
            
        return max_length