class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        dp = [0, 0, 0]
        n = len(stoneValue)
        
        for i in range(n - 1, -1, -1):
            ans = stoneValue[i] - dp[0]
            if i + 2 <= n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] - dp[1])
            if i + 3 <= n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[2])
            
            dp = [ans, dp[0], dp[1]]
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"