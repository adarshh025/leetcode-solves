from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        val_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            val_to_indices[val].append(i)
            
        visited = [False] * n
        visited[0] = True
        queue = deque([(0, 0)])
        
        while queue:
            idx, steps = queue.popleft()
            
            if idx == n - 1:
                return steps
                
            for neighbor in val_to_indices[arr[idx]]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, steps + 1))
                    
            val_to_indices[arr[idx]].clear()
            
            if idx + 1 < n and not visited[idx + 1]:
                visited[idx + 1] = True
                queue.append((idx + 1, steps + 1))
                
            if idx - 1 >= 0 and not visited[idx - 1]:
                visited[idx - 1] = True
                queue.append((idx - 1, steps + 1))
                
        return -1