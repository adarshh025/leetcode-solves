from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board into a single string
        start_state = "".join(str(val) for row in board for val in row)
        target = "123450"
        
        # Valid swap indices for the '0' at each string index
        # e.g., if '0' is at index 0, it can swap with indices 1 and 3
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # Queue stores tuples of (board_state, moves_count)
        queue = deque([(start_state, 0)])
        visited = set([start_state])
        
        while queue:
            curr_state, moves = queue.popleft()
            
            if curr_state == target:
                return moves
            
            # Find where the empty space '0' is located
            zero_idx = curr_state.index('0')
            
            # Try all valid moves
            for next_idx in neighbors[zero_idx]:
                # Swap the characters
                state_list = list(curr_state)
                state_list[zero_idx], state_list[next_idx] = state_list[next_idx], state_list[zero_idx]
                next_state = "".join(state_list)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, moves + 1))
                    
        return -1
