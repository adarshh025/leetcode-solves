from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')
        
        if cnt0 == 0:
            return 0
            
        # DSU to skip visited nodes. Steps of 2 ensure parity is strictly maintained.
        parent = list(range(n + 3))
        
        # Iterative path-halving to find the next available unvisited zero-count
        def find(i: int) -> int:
            curr = i
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
            
        q = deque([cnt0])
        parent[cnt0] = cnt0 + 2
        ans = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return ans
                    
                min_x = max(0, k - n + cur)
                max_x = min(cur, k)
                
                # Smallest and largest number of 0s possible in the next step
                l = cur + k - 2 * max_x
                r = cur + k - 2 * min_x
                
                # Instantly skip over counts we've already queued
                curr_nxt = find(l)
                while curr_nxt <= r:
                    q.append(curr_nxt)
                    parent[curr_nxt] = curr_nxt + 2
                    curr_nxt = find(curr_nxt)
                    
            ans += 1
            
        return -1