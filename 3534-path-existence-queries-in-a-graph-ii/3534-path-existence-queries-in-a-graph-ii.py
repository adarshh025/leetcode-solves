from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Store original indices alongside values, then sort
        sorted_nodes = sorted([(nums[i], i) for i in range(n)])
        
        # Map original indices to their new positions in the sorted array
        pos = [0] * n
        for i in range(n):
            pos[sorted_nodes[i][1]] = i
            
        LOG = 18  # 2^17 > 100,000 (enough to cover maximum possible jumps)
        up = [[0] * LOG for _ in range(n)]
        
        # 2. Two pointers to find the furthest reachable node in exactly 1 step
        right = 0
        for left in range(n):
            while right < n and sorted_nodes[right][0] - sorted_nodes[left][0] <= maxDiff:
                right += 1
            up[left][0] = right - 1
            
        # 3. Build the binary lifting table (furthest jump in 2^j steps)
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # 4. Process each query in O(log N)
        ans = []
        for u, v in queries:
            posU, posV = pos[u], pos[v]
            
            # Same node
            if posU == posV:
                ans.append(0)
                continue
                
            # Ensure we always jump left-to-right
            if posU > posV:
                posU, posV = posV, posU
                
            curr = posU
            steps = 0
            
            # Greedily jump as close to posV as possible WITHOUT overshooting it
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < posV:
                    curr = up[curr][j]
                    steps += (1 << j)
                    
            # Check if we can close the final gap in one last jump
            if up[curr][0] >= posV:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans