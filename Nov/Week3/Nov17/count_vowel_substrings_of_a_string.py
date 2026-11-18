class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        last_s = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1}
        last_c = -1
        count = 0
        for i, char in enumerate(word):
            if char in vowels:
                last_s[char] = i
                all_v = min(last_s.values())
                if all_v > last_c:
                    count += all_v - last_c
            else:
                last_c = i
        return count