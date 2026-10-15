class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_len = 0
        mp = {}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            rem = prefix_sum - k

            if rem in mp:
                max_len = max(max_len, i - mp[rem])

            if prefix_sum not in mp:
                mp[prefix_sum] = i

        return max_len