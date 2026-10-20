class Solution:
    def inversionCount(self, arr):
        _, count = self.mergeSort(arr)
        return count

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left, inv1 = self.mergeSort(arr[:mid])
        right, inv2 = self.mergeSort(arr[mid:])

        merged, inv3 = self.merge(left, right)

        return merged, inv1 + inv2 + inv3

    def merge(self, left, right):
        i = j = 0
        inv = 0
        ans = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                inv += len(left) - i
                j += 1

        while i < len(left):
            ans.append(left[i])
            i += 1

        while j < len(right):
            ans.append(right[j])
            j += 1

        return ans, inv