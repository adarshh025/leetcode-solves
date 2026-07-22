class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left, stopping just before the MSB (index 0)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            # If the bit plus the carry results in 1, the current value is odd
            if bit + carry == 1:
                # Odd requires +1 (which triggers a carry) then /2
                steps += 2
                carry = 1
            else:
                # Even (0 + 0 = 0, or 1 + 1 = 2 with existing carry) 
                # just requires /2
                steps += 1
                
        # The MSB is always '1'. If we carry over a 1 to it, 
        # it becomes 2 (binary 10), requiring exactly 1 extra division step.
        return steps + carry