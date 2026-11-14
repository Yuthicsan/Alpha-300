class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def matches(word: str, pat: str) -> bool:
            if len(word) != len(pat):
                return False
                
            w_to_p = {}
            p_to_w = {}
            
            for cw, cp in zip(word, pat):
                if cw in w_to_p and w_to_p[cw] != cp:
                    return False
                if cp in p_to_w and p_to_w[cp] != cw:
                    return False
                    
                w_to_p[cw] = cp
                p_to_w[cp] = cw
                
            return True

        return [w for w in words if matches(w, pattern)]