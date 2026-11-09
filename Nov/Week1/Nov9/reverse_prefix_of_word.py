class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chars = list(word)
        n = len(chars)
        idx = -1
        for i in range(n):
            if chars[i] == ch:
                idx = i
                break
        if idx != -1:
            left = 0
            right = idx
            while left < right:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left += 1
                right -= 1
        return "".join(chars)