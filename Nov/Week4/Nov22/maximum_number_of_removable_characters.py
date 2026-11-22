class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        l=0
        r=len(removable)-1
        def subseq(mid):
            i=0
            rem=set(removable[:mid+1])
            for j in range(len(s)):
                if j in rem:
                    continue
                if i<len(p) and s[j]==p[i]:
                    i+=1
            if i==len(p):
                return True
            return False
        while l<=r:
            mid=(l+r)//2
            if subseq(mid):
                l=mid+1
            else:
                r=mid-1
        return l

        