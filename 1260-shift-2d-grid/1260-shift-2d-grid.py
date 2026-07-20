from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total  # Avoid unnecessary full-grid rotations
        
        # If no effective shifts are needed, return the original grid
        if k == 0:
            return grid
            
        # Create an empty grid of the same dimensions
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Calculate the 1D index
                curr_idx = r * n + c
                
                # Shift the 1D index
                new_idx = (curr_idx + k) % total
                
                # Convert back to 2D coordinates and place the value
                new_r = new_idx // n
                new_c = new_idx % n
                result[new_r][new_c] = grid[r][c]
                
        return result