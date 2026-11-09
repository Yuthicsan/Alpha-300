class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(chars) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            if left < right:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left += 1
                right -= 1
        return "".join(chars)