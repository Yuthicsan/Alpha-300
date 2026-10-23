class Solution:
    def rowWithMax1s(self, arr: list[list[int]]) -> int:
        n = len(arr)
        m = len(arr[0])

        max_row = -1
        leftmost = m

        for i in range(n):
            low, high = 0, m - 1
            first_one = m

            while low <= high:
                mid = (low + high) // 2

                if arr[i][mid] == 1:
                    first_one = mid
                    high = mid - 1
                else:
                    low = mid + 1

            if first_one < leftmost:
                leftmost = first_one
                max_row = i

        return max_row