class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        bit_length = 0
        
        for i in range(1, n + 1):
            # If 'i' is a power of 2, its binary representation needs one more bit
            if (i & (i - 1)) == 0:
                bit_length += 1
            
            # Shift the current answer left by 'bit_length' spaces 
            # and use bitwise OR to append 'i' to the empty spaces
            ans = ((ans << bit_length) | i) % MOD
            
        return ans