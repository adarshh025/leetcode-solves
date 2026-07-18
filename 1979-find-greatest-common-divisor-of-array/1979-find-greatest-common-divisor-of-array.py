import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find the smallest and largest numbers
        smallest = min(nums)
        largest = max(nums)
        
        # Return their greatest common divisor
        return math.gcd(smallest, largest)