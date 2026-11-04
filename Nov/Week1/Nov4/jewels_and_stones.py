class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        for ch in jewels:
            freq[ch] = 1
        count = 0
        for ch in stones:
            if ch in freq:
                count += 1
        return count