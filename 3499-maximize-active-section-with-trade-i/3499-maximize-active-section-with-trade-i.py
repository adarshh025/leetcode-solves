class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = 0
        mx = 0
        pre = float('-inf')
        
        i = 0
        n = len(s)
        
        while i < n:
            j = i
            
            # Group identical contiguous characters
            while j < n and s[j] == s[i]:
                j += 1
                
            cur = j - i
            
            if s[i] == '1':
                ans += cur
            else:
                # Calculate the optimal merge of two adjacent '0' blocks
                mx = max(mx, pre + cur)
                pre = cur
                
            i = j
            
        return ans + mx