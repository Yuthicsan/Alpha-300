class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ """
        n = len(s)
        freqt = defaultdict(int) # pyright: ignore[reportUndefinedVariable]
        freqm = defaultdict(int) # type: ignore

        for c in t:
            freqt[c] += 1

        l = 0
        reqt = len(freqt)
        reqm = 0
        minlen = float("inf")
        res = [-1, -1]
        for r in range(n):
            c = s[r]
            if c in freqt:
                freqm[c] += 1
                if freqm[c] == freqt[c]:
                    reqm += 1
                    while reqm == reqt:
                        if r - l + 1 < minlen:
                            minlen = r - l + 1
                            res = [l, r]
                        c = s[l]
                        if c in freqm:
                            freqm[c] -= 1
                            if freqm[c] < freqt[c]:
                                reqm -= 1
                        l += 1
        return s[res[0] : res[1] + 1]