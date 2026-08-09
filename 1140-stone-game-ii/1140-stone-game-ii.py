from typing import List
from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = piles[:]
        
        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]
            
        @cache
        def dp(i, m):
            if i + 2 * m >= n:
                return suffix[i]
            
            return suffix[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        
        return dp(0, 1)