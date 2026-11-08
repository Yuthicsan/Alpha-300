class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        if not words:
            return ""
        chars = list(" ".join(words))
        n = len(chars)
        chars.reverse()
        left = 0
        right = 0
        i = 0
        while i < n:
            while i < n and chars[i] == ' ':
                i += 1
            if i == n:
                break
            if right > 0:
                chars[right] = ' '
                right += 1
            left = right
            while i < n and chars[i] != ' ':
                chars[right] = chars[i]
                right += 1
                i += 1
            chars[left:right] = reversed(chars[left:right])
        return "".join(chars[:right])