class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        freq = {}
        for w in words:
            cur = freq
            for c in w:
                if c not in cur:
                    cur[c] = {"@": 0}
                cur = cur[c]
                cur["@"]+=1
            cur["#"]= True
        res = []
        for w in words:
            score = 0
            cur = freq
            invalid = False
            for c in w:
                if c not in cur:
                    invalid=True
                    break
                cur = cur[c]
                score+=cur["@"] if "@" in cur else 0
            if invalid:
                res.append(0)
            else:
                res.append(score)
        return res