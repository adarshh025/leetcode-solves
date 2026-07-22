class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Number of required distinct binary codes of length k
        required_count = 1 << k  # Equivalent to 2^k
        
        # Early exit: If the string is too short to even contain 'required_count' substrings
        if len(s) - k + 1 < required_count:
            return False
            
        seen = set()
        
        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            seen.add(s[i : i + k])
            
            # If we've found all combinations, we can stop early
            if len(seen) == required_count:
                return True
                
        return False