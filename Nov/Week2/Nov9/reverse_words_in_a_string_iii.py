class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                left = start
                right = i - 1
                while left < right:
                    temp = chars[left]
                    chars[left] = chars[right]
                    chars[right] = temp
                    left += 1
                    right -= 1
                start = i + 1
        return "".join(chars)