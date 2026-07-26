import math
from collections import defaultdict
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        dp = defaultdict(int)
        dp[(0, 0)] = 1
        
        for x in nums:
            new_dp = defaultdict(int, dp)
            for (g1, g2), count in dp.items():
                ng1 = math.gcd(g1, x)
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + count) % MOD
                
                ng2 = math.gcd(g2, x)
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + count) % MOD
                
            dp = new_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans