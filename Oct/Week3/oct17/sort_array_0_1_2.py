class Solution(object):
    def sortColors(self, nums):
        c0 = c1 = c2 = 0
        for x in nums:
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
            else:
                c2 += 1
        i = 0
        while c0:
            nums[i] = 0
            i += 1
            c0 -= 1
        while c1:
            nums[i] = 1
            i += 1
            c1 -= 1
        while c2:
            nums[i] = 2
            i += 1
            c2 -= 1
        return nums