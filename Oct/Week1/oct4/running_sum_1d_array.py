class Solution(object):
    def runningSum(self, nums):
        x = 0
        m = []
        for i in nums :
            x = x + i
            m.append(x)
        return m