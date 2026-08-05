class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        n = len(nums)
        # Using arrays instead of dicts for O(1) lookups and better memory locality
        first = [-1] * (n + 1)
        second = [-1] * (n + 1)
        ans = float('inf')
        
        for i, val in enumerate(nums):
            if second[val] != -1:
                # If we've seen it twice before, the distance is 2 * (rightmost - leftmost)
                ans = min(ans, 2 * (i - first[val]))
                
                # Slide the window to the two most recent occurrences
                first[val] = second[val]
                second[val] = i
            elif first[val] != -1:
                second[val] = i
            else:
                first[val] = i
                
        return ans if ans != float('inf') else -1