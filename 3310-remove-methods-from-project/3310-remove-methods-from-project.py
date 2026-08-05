class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        suspicious = {k}
        q = [k]
        
        for u in q:
            for v in adj[u]:
                if v not in suspicious:
                    suspicious.add(v)
                    q.append(v)
                    
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
                
        return [i for i in range(n) if i not in suspicious]