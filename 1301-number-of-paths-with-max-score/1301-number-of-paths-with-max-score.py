from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == n - 1 and c == n - 1) or board[r][c] == 'X':
                    continue
                    
                max_prev = max(dp[r + 1][c][0], dp[r][c + 1][0], dp[r + 1][c + 1][0])
                
                if max_prev == -1:
                    continue
                    
                ways = 0
                if dp[r + 1][c][0] == max_prev:
                    ways = (ways + dp[r + 1][c][1]) % MOD
                if dp[r][c + 1][0] == max_prev:
                    ways = (ways + dp[r][c + 1][1]) % MOD
                if dp[r + 1][c + 1][0] == max_prev:
                    ways = (ways + dp[r + 1][c + 1][1]) % MOD
                    
                val = 0 if board[r][c] == 'E' else int(board[r][c])
                dp[r][c] = [max_prev + val, ways]
                
        return [dp[0][0][0], dp[0][0][1]] if dp[0][0][0] != -1 else [0, 0]