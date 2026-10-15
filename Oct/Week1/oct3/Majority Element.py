class Solution(object):
    def majorityElement(self, nums):
        count = 0 
        final = None
        for i in nums :
            if count == 0:
                final = i
            if final == i:
                count += 1
            if final != i:
                count -= 1
        return final