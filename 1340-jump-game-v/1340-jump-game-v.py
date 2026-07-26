from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        
        for _, i in sorted((arr[i], i) for i in range(n)):
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
        return max(dp)