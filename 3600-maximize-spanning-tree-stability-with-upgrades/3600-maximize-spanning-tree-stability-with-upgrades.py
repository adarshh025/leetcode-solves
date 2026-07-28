class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.cc = size
                
            def find(self, x):
                curr = x
                while curr != self.parent[curr]:
                    self.parent[curr] = self.parent[self.parent[curr]]
                    curr = self.parent[curr]
                return curr
                
            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx != ry:
                    self.parent[rx] = ry
                    self.cc -= 1
                    return True
                return False

        uf_all = UnionFind(n)
        uf_req = UnionFind(n)
        mn_req = float('inf')
        
        for u, v, s, must in edges:
            uf_all.union(u, v)
            if must == 1:
                if not uf_req.union(u, v):
                    return -1
                mn_req = min(mn_req, s)
                
        if uf_all.cc > 1:
            return -1
            
        def check(lim):
            if lim > mn_req:
                return False
                
            uf = UnionFind(n)
            
            for u, v, s, must in edges:
                if must == 1:
                    uf.union(u, v)
                    
            for u, v, s, must in edges:
                if must == 0 and s >= lim:
                    uf.union(u, v)
                    
            upgrades = 0
            for u, v, s, must in edges:
                if must == 0 and s < lim and 2 * s >= lim:
                    if uf.union(u, v):
                        upgrades += 1
                        
            return uf.cc == 1 and upgrades <= k

        low = 1
        high = mn_req if mn_req != float('inf') else max((s * 2 for _, _, s, _ in edges), default=0)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return int(ans)