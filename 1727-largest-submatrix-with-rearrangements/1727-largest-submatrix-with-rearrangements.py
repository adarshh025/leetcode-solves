class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
                    
            curr_row = sorted(matrix[i], reverse=True)
            for j in range(n):
                ans = max(ans, curr_row[j] * (j + 1))
                
        return ans