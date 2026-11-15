class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if n_len == 0:
            return 0    
        for i in range(h_len - n_len + 1):
            match = True
            for j in range(n_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1