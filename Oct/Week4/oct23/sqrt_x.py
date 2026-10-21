class Solution(object):
    def mySqrt(self, x):
        l = 1
        r = x
        while l<=r:
            mid = (r + l)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid+1
            else : 
                r = mid - 1
        return r