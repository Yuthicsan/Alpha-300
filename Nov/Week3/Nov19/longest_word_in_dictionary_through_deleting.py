class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        ans = ""
        for word in dictionary:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans): continue
            pos = -1
            for char in word:
                pos = s.find(char, pos + 1)
                if pos == -1: break
            else: ans = word
        return ans