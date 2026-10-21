class Solution(object):
    def isPerfectSquare(self, num):
        l = 1
        r = num
        while l<=r:
            mid = (r + l)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l = mid+1
            else : 
                r = mid - 1
        return False