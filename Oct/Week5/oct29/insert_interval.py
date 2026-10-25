class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)

        intervals = self.mergeSort(intervals)

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.mergeArrays(left, right)

    def mergeArrays(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result