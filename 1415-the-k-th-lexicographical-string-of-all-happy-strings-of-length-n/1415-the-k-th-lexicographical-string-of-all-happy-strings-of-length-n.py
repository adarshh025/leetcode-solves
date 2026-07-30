class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
            
        ans = []
        k -= 1
        
        ans.append("abc"[k // (1 << (n - 1))])
        k %= 1 << (n - 1)
        
        for i in range(n - 1):
            choices = [c for c in "abc" if c != ans[-1]]
            idx = k // (1 << (n - 2 - i))
            ans.append(choices[idx])
            k %= 1 << (n - 2 - i)
            
        return "".join(ans)