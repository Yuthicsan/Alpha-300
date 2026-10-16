class Solution(object):
    def removeElement(self, nums, val):
        p = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[p] = nums[i]
                p += 1
        return p