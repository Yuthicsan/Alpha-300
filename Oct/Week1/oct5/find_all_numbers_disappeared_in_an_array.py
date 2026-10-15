class Solution(object):
    def findDisappearedNumbers(self, nums):
        mp = {}

        for num in nums:
            mp[num] = 1

        ans = []

        for i in range(1, len(nums) + 1):
            if i not in mp:
                ans.append(i)

        return ans