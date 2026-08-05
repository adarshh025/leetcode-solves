class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        
        for i in range(len(mat)):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
                    
        return True
        