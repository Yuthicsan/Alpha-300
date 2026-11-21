class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=[]
        c=0
        for i in range(len(s)):
            l.append(set(s[i:i+3]))
        for j in l:
            if len(j)==3:
                c+=1
        return c
        