class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for x,i in enumerate(s):
            if freq[i] == 1:
                return x
        return -1 