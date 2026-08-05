class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        top, bottom = x, x + k - 1
        while top < bottom:
            grid[top][y:y+k], grid[bottom][y:y+k] = grid[bottom][y:y+k], grid[top][y:y+k]
            top += 1
            bottom -= 1
            
        return grid