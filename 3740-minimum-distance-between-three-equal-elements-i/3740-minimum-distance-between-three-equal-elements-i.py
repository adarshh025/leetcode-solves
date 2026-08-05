class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        n = len(nums)
       
        first = [-1] * (n + 1)
        second = [-1] * (n + 1)
        ans = float('inf')
        
        for i, val in enumerate(nums):
            if second[val] != -1:
               
                ans = min(ans, 2 * (i - first[val]))
                
              
                first[val] = second[val]
                second[val] = i
            elif first[val] != -1:
                second[val] = i
            else:
                first[val] = i
                
        return ans if ans != float('inf') else -1