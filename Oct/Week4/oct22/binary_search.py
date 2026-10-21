class Solution:
    def binarySearch(self, arr: list[int], k: int) -> int:
            n = len(arr)
            l = 0
            r = n-1
            while l<=r:
                mid = (r + l)//2
                if arr[mid] == k:
                    return mid
                elif arr[mid] < k:
                    l = mid+1
                else : 
                    r = mid - 1
            return -1