# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#     def get(self, index):
#         pass
#
#     def length(self):
#         pass

class Solution(object):
    def findInMountainArray(self, target, mountainArr):

        def find_peak():
            left, right = 0, mountainArr.length() - 1

            while left < right:
                mid = left + (right - left) // 2

                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid

            return left

        def binary_search(left, right, ascending=True):
            while left <= right:
                mid = left + (right - left) // 2
                value = mountainArr.get(mid)

                if value == target:
                    return mid

                if ascending:
                    if value < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if value < target:
                        right = mid - 1
                    else:
                        left = mid + 1

            return -1

        peak = find_peak()

        ans = binary_search(0, peak, True)
        if ans != -1:
            return ans

        return binary_search(
            peak + 1,
            mountainArr.length() - 1,
            False
        )
    