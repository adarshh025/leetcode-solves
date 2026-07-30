class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                
                L = 1
                while i + 2 * L < m and j - L >= 0 and j + L < n:
                    curr = 0
                    for k in range(L):
                        curr += grid[i + k][j + k]
                    for k in range(L):
                        curr += grid[i + L + k][j + L - k]
                    for k in range(L):
                        curr += grid[i + 2 * L - k][j - k]
                    for k in range(L):
                        curr += grid[i + L - k][j - L + k]
                        
                    sums.add(curr)
                    L += 1
                    
        return sorted(list(sums), reverse=True)[:3]