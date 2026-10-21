class Solution(object):
    def binSearch(self , nums , target, leftBias):
        l = 0
        r = len(nums) -1
        i = -1
        while l<=r:
            mid = (r + l)//2
            if nums[mid] == target:
                i = mid
                if leftBias:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid] < target:
                l = mid+1
            else : 
                r = mid - 1
        return i
    def searchRange(self, nums, target):
        left = self.binSearch(nums , target, True)
        right = self.binSearch(nums , target, False)
        return [left , right]
