class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        total_len = n + m - 1
        
        word = ['?'] * total_len
        fixed = [False] * total_len
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if word[idx] == '?':
                        word[idx] = str2[j]
                        fixed[idx] = True
                    elif word[idx] != str2[j]:
                        return ""
                        
        for i in range(total_len):
            if word[i] == '?':
                word[i] = 'a'
                
        str2_list = list(str2)
        for i in range(n):
            if str1[i] == 'F':
                if word[i:i+m] == str2_list:
                    changed = False
                    for j in range(i + m - 1, i - 1, -1):
                        if not fixed[j]:
                            word[j] = 'b'
                            fixed[j] = True
                            changed = True
                            break
                    
                    if not changed:
                        return ""
                        
        return "".join(word)