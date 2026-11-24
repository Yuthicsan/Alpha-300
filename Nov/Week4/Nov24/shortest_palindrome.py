class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        rev = s[::-1]
        t = s + '#' + rev
        l = [0] * len(t)
        le = 0
        i = 1
        while i < len(t):
            if t[i] == t[le]:
                le += 1
                l[i] = le
                i+=1
            elif le != 0:
                le = l[le-1]
            else:
                l[i] = 0
                i+=1
        k = l[-1]
        return rev[:len(s) - k] + s