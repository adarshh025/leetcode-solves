import bisect
from typing import List

class SparseTable:
    def __init__(self, data: List[int]):
        self.n = len(data)
        if self.n == 0:
            return
        self.log = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.log)]
        self.st[0] = data[:]
        for i in range(1, self.log):
            length = 1 << (i - 1)
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + length])

    def query(self, L: int, R: int) -> int:
        if L > R or L < 0 or R >= self.n:
            return 0
        i = (R - L + 1).bit_length() - 1
        return max(self.st[i][L], self.st[i][R - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # 1. Total '1's in the entire string
        pref_ones = [0] * (n + 1)
        for i in range(n):
            pref_ones[i + 1] = pref_ones[i] + (1 if s[i] == '1' else 0)
            
        total_ones = pref_ones[n]
        
        # 2. Extract zero-groups: (start_index, end_index, length)
        zero_groups = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zero_groups.append((start, i - 1, i - start))
            else:
                i += 1

        m = len(zero_groups)
        
        # If there are fewer than 2 zero-groups anywhere, NO trade is possible.
        if m < 2:
            return [total_ones] * len(queries)

        group_starts = [g[0] for g in zero_groups]
        group_ends = [g[1] for g in zero_groups]

        # 3. Adjacent lengths sum array & Sparse Table initialization
        adj_sums = [zero_groups[k][2] + zero_groups[k + 1][2] for k in range(m - 1)]
        st = SparseTable(adj_sums)

        ans = []

        # 4. Process each query
        for l, r in queries:
            # Find which zero-groups overlap with [l, r]
            first_idx = bisect.bisect_left(group_ends, l)
            last_idx = bisect.bisect_right(group_starts, r) - 1

            # Valid trades require at least TWO zero-groups inside the substring
            if first_idx >= last_idx or first_idx >= m or last_idx < 0:
                ans.append(total_ones)
                continue

            # Start with the baseline: 1s in the entire original string
            max_active = total_ones

            # Lengths of boundary zero-groups trimmed by l and r limits
            left_len = min(zero_groups[first_idx][1], r) - max(zero_groups[first_idx][0], l) + 1
            right_len = min(zero_groups[last_idx][1], r) - max(zero_groups[last_idx][0], l) + 1

            # Option 1: Exactly 2 overlapping zero-groups
            if first_idx + 1 == last_idx:
                max_active = max(max_active, total_ones + left_len + right_len)
                
            # Option 2: 3 or more overlapping zero-groups
            else:
                # Merge trimmed left group with its next full adjacent group
                max_active = max(max_active, total_ones + left_len + zero_groups[first_idx + 1][2])
                
                # Merge trimmed right group with its previous full adjacent group
                max_active = max(max_active, total_ones + right_len + zero_groups[last_idx - 1][2])
                
                # Query any internal pairs of fully contained adjacent zero-groups
                if first_idx + 1 <= last_idx - 2:
                    best_internal = st.query(first_idx + 1, last_idx - 2)
                    max_active = max(max_active, total_ones + best_internal)

            ans.append(max_active)

        return ans