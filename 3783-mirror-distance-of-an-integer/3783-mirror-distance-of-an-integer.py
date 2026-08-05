class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reversed_n = 0
        
        while n > 0:
            reversed_n = reversed_n * 10 + n % 10
            n //= 10
            
        return abs(original - reversed_n)