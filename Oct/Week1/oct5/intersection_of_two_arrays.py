class Solution(object):
    def intersection(self, nums1, nums2):
        freq = {}
        for x in nums1:
            freq[x] = 1
        result = []
        for x in nums2 :
            if x in freq and freq[x] == 1:
                result.append(x)
                freq[x] = 0
        return result
