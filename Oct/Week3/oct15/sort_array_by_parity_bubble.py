class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)
        for i in range (n-1):
            for j in range(n-i-1):
                if nums[j] % 2 == 1 and nums[j+1] % 2 == 0:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
        return nums