class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if not s:
            return s
        l, r = 0, len(s)-1
        res = list(s)
        def check_ascii(s):
            if 'a' <= s <= 'z' or 'A' <= s <= 'Z':
                return True
            return False
        while l < r:
            while l < r and not check_ascii(s[l]):
                l += 1
            while l < r and not check_ascii(s[r]):
                r -= 1            
            if l < r:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -=1
        return "".join(res)
