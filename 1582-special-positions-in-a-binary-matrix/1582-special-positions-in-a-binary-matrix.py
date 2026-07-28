class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(col) for col in zip(*mat)]
        
        res = 0
        for i in range(len(mat)):
            if row_sums[i] == 1:
                for j in range(len(mat[0])):
                    if mat[i][j] == 1 and col_sums[j] == 1:
                        res += 1
                        
        return res