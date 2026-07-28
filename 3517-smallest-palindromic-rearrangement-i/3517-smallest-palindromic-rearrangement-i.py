from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        
        half = []
        mid = ""
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq[char] > 0:
                half.append(char * (freq[char] // 2))
                if freq[char] % 2 != 0:
                    mid = char
                    
        first_half = "".join(half)
        return first_half + mid + first_half[::-1]