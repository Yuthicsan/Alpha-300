class Solution:
    def countFreq(self, nums, target):
        left = self.binSearch(nums , target, True)
        if left == -1:
            return 0
        right = self.binSearch(nums , target, False)
        return right-left+1 

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
        