class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l < r:
            mid = (l+r)//2
            if isBadVersion(mid): # type: ignore
                r = mid
            else:
                l = mid+1
        return l