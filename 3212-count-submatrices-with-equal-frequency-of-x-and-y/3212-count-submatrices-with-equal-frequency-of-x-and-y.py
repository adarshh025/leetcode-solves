class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        prev_x = [0] * n
        prev_y = [0] * n
        
        for i in range(m):
            curr_x = 0
            curr_y = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    curr_x += 1
                elif grid[i][j] == 'Y':
                    curr_y += 1
                    
                prev_x[j] += curr_x
                prev_y[j] += curr_y
                
                if prev_x[j] > 0 and prev_x[j] == prev_y[j]:
                    ans += 1
                    
        return ans