from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort using a tuple: (number of 1 bits, the number itself)
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr