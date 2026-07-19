from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
        
        # We only need to check 'word_len' different alignments
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            words_used = 0
            
            # Slide the window in steps of 'word_len'
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    # If we have more of this word than needed, shrink the window from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                        
                    # If we used exactly the required number of words, record the start index
                    if words_used == num_words:
                        result.append(left)
                else:
                    # Chain broken; clear the current window and move left pointer
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return result