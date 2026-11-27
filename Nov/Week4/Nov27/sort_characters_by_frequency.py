from collections import Counter
class Solution(object):
    def rearrangeCharacters(self, s, target):
        k=""
        for x in s:
            if x in target: k+=x
        a=Counter(k)
        b=Counter(target)
        m=float('inf')
        for x in b: m=min(m,a[x]//b[x])
        return m