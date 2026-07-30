class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                top = grid[i - 1][j] if i > 0 else 0
                left = grid[i][j - 1] if j > 0 else 0
                top_left = grid[i - 1][j - 1] if i > 0 and j > 0 else 0
                
                grid[i][j] += top + left - top_left
                
                if grid[i][j] <= k:
                    ans += 1
                else:
                    break
                    
        return ans