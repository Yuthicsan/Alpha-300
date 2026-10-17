class Solution(object):
    def sortedSquares(self, nums):
        ans = []
        l = 0
        r = len(nums)-1
        while l<=r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left > right:
                ans.insert(0 , left**2)
                l+=1
            else:
                ans.insert(0 , right**2)
                r-=1
        return ans