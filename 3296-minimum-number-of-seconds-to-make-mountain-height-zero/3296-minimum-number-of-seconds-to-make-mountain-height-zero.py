import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        left = 1
        right = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            total = 0
            
            for w in workerTimes:
                total += (math.isqrt(1 + 8 * (mid // w)) - 1) // 2
                if total >= mountainHeight:
                    break
            
            if total >= mountainHeight:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans