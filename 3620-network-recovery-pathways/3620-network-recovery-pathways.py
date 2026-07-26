import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        costs = set()
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            costs.add(cost)
            
        unique_costs = sorted(list(costs))
        ans = -1
        low, high = 0, len(unique_costs) - 1
        
        def check(min_w):
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > dist[u]:
                    continue
                    
                if u == n - 1:
                    return True
                    
                for v, cost in adj[u]:
                    if cost >= min_w and online[v]:
                        new_d = d + cost
                        if new_d < dist[v] and new_d <= k:
                            dist[v] = new_d
                            heapq.heappush(pq, (new_d, v))
                            
            return False
            
        while low <= high:
            mid = (low + high) // 2
            if check(unique_costs[mid]):
                ans = unique_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans