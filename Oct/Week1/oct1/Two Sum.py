class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range (len(nums)):
            value = nums[i]
            diff = target - value
            if value in d :
                return [i , d[value]]
            else:
                d[diff] = i
        d[diff] = i
            