class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = self.mergeSort(intervals)

        count = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prevEnd:
                count += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return count

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