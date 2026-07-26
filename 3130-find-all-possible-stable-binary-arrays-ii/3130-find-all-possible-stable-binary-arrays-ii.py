class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        MAX = max(zero, one) + 2
        
        # Precompute factorials and their modular inverses for O(1) combinations
        fact = [1] * MAX
        inv = [1] * MAX
        for i in range(1, MAX):
            fact[i] = (fact[i - 1] * i) % MOD
            
        inv[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
        for i in range(MAX - 2, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % MOD
            
        # Combinatorial generation instead of 2D DP to prevent MemoryError
        def get_W(N: int):
            W = [0] * (N + 2)
            # Short-circuit worst-case execution for limit = 1
            if limit == 1:
                if N < len(W): W[N] = 1
                return W
                
            for K in range(1, N + 2):
                res = 0
                max_j = min((N - K) // limit, K)
                if max_j < 0:
                    W[K] = 0
                    continue
                
                inv_K_minus_1 = inv[K - 1]
                fact_K = fact[K]
                
                for j in range(max_j + 1):
                    term = (fact_K * inv[j] % MOD) * inv[K - j] % MOD
                    rem = N - j * limit
                    term2 = (fact[rem - 1] * inv_K_minus_1 % MOD) * inv[rem - K] % MOD
                    
                    if j % 2 == 1:
                        res = (res - term * term2) % MOD
                    else:
                        res = (res + term * term2) % MOD
                        
                W[K] = res
            return W
            
        W_zero = get_W(zero)
        W_one = get_W(one)
        
        ans = 0
        for K in range(1, min(zero, one) + 2):
            w_z = W_zero[K]
            w_z_minus = W_zero[K - 1]
            w_o = W_one[K]
            w_o_minus = W_one[K - 1]
            
            # Starts with 0, ends with 1 
            # Starts with 1, ends with 0 
            # Starts with 0, ends with 0
            # Starts with 1, ends with 1
            ans = (ans + w_z * w_o * 2 + w_z * w_o_minus + w_z_minus * w_o) % MOD
            
        return ans