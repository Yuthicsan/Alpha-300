class Solution:
    def sortInWave(self, nums):
        for i in range(len(nums) - 1):

            if i % 2 == 1:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    
        return nums