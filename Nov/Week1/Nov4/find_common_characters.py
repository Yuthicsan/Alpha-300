class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        freq = {}

        for ch in words[0]:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for word in words[1:]:
            curr = {}
            for ch in word:
                if ch in curr:
                    curr[ch] += 1
                else:
                    curr[ch] = 1
            new_freq = {}
            for ch in freq:
                if ch in curr:
                    new_freq[ch] = min(freq[ch], curr[ch])
            freq = new_freq
        ans = []
        for ch in freq:
            for _ in range(freq[ch]):
                ans.append(ch)
        return ans