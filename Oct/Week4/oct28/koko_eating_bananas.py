class Solution:
    def minEatingSpeed(self, piles, h):
        def can(speed):
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            return hours <= h

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans