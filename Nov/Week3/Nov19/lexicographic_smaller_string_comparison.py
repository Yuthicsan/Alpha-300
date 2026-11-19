class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        pos = {}
        n = len(words)
        for i, ch in enumerate(order):
            pos[ch] = i
        for i in range(1, n):
            w1 = words[i - 1]
            w2 = words[i]
            j = 0
            while j < len(w1) and j < len(w2):
                if pos[w1[j]] < pos[w2[j]]:
                    break
                elif pos[w1[j]] > pos[w2[j]]:
                    return False
                j += 1
            if j == len(w2) and len(w1) > len(w2):
                return False
        return True