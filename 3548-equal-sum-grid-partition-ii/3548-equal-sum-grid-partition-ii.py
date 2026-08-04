from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        def check(g: list[list[int]]) -> bool:
            m, n = len(g), len(g[0])
            total_sum = sum(sum(row) for row in g)
            
            top_sum = 0
            top_freq = defaultdict(int)
            bottom_freq = defaultdict(int)
            
            for r in range(m):
                for c in range(n):
                    bottom_freq[g[r][c]] += 1
                    
            for i in range(m - 1):
                for c in range(n):
                    val = g[i][c]
                    top_freq[val] += 1
                    bottom_freq[val] -= 1
                    if bottom_freq[val] == 0:
                        del bottom_freq[val]
                    top_sum += val
                    
                bottom_sum = total_sum - top_sum
                diff = top_sum - bottom_sum
                
                if diff == 0:
                    return True
                    
                if diff > 0:
                    target = diff
                    R = i + 1
                    if R > 1 and n > 1:
                        if target in top_freq: return True
                    elif R == 1 and n > 1:
                        if g[0][0] == target or g[0][-1] == target: return True
                    elif n == 1 and R > 1:
                        if g[0][0] == target or g[i][0] == target: return True
                else:
                    target = -diff
                    R = m - 1 - i
                    if R > 1 and n > 1:
                        if target in bottom_freq: return True
                    elif R == 1 and n > 1:
                        if g[i+1][0] == target or g[i+1][-1] == target: return True
                    elif n == 1 and R > 1:
                        if g[i+1][0] == target or g[m-1][0] == target: return True
                        
            return False

        def rotate(g: list[list[int]]) -> list[list[int]]:
            return [list(x) for x in zip(*g[::-1])]
            
        return check(grid) or check(rotate(grid))