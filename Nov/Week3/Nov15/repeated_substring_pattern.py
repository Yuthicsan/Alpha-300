class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for l in range(1, n // 2 + 1):
            if n % l == 0:
                sub = s[:l]
                constructed = []
                for _ in range(n // l):
                    constructed.append(sub)
                if "".join(constructed) == s:
                    return True
        return False