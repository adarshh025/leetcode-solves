class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def dfs(n, k):
            if n == 1:
                return "0"
            
            length = (1 << n) - 1
            mid = length // 2 + 1
            
            if k == mid:
                return "1"
            elif k < mid:
                return dfs(n - 1, k)
            else:
                return "0" if dfs(n - 1, length - k + 1) == "1" else "1"
                
        return dfs(n, k)