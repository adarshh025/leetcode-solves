class Solution:
    def minOperations(self, s: str) -> int:
      
        diff = sum(1 for i, c in enumerate(s) if str(i % 2) != c)
        
       
        return min(diff, len(s) - diff)