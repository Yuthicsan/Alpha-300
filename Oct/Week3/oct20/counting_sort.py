class Solution:
    def countingSort(self,arr):
        min_val = min(arr)
        max_val = max(arr)
        k = max_val - min_val + 1
        count = [0] * k
        for i in arr:
            index = i - min_val
            count[index] += 1
        result = []
        for i in range(0 , k):
            num = i + min_val
            freq = count[i]
            result.extend([num] * freq)
        return result