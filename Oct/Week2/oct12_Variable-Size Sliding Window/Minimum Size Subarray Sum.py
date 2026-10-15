class Solution(object):
    def minSubArrayLen(self, target, nums):
        minlen=float("inf")
        length=0
        sum1=0
        left=0
        for  right in range(len(nums)):
            sum1+=nums[right]
            while sum1>=target:
                length=right-left+1
                if length<minlen:
                    minlen=length
                sum1=sum1-nums[left]
                left+=1
        if minlen==float("inf"):
            return 0
        return minlen
        