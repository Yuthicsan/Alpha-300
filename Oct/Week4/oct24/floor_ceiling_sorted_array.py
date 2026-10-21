class Solution:
    def findCeil(self, arr, target):
        # code here
        l, r = 0, len(arr) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] < target:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1

        return ans

class Solution:
    def findFloor(self, arr, target):
        l, r = 0, len(arr) - 1
        ans = -1
    
        while l <= r:
            mid = (l + r) // 2
    
            if arr[mid] <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
    
        return ans