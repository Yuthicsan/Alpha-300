class Solution(object):
    def moveZeroes(self, nums):
        a = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] , nums[a] = nums[a] , nums[i]
                a+=1        