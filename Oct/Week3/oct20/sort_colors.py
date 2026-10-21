class Solution(object):
    def sortColors(self, nums):
        l = 0
        h = len(nums) - 1
        mid = 0
        while mid <= h:
            if nums[mid] == 0:
                nums[l] , nums[mid] = nums[mid] , nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                 nums[h] , nums[mid] = nums[mid] , nums[h]
                 h -= 1
        return nums