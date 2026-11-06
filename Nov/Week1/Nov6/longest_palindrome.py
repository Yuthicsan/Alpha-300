class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_c = 0
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_c += 1
            else:
                odd_c -= 1
        if odd_c > 1:
            return len(s) - odd_c + 1
        return len(s)