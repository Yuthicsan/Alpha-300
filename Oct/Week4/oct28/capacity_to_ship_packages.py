class Solution:
    def shipWithinDays(self, weights, days):
        def can(cap):
            needed_days = 1
            curr = 0

            for w in weights:
                if curr + w > cap:
                    needed_days += 1
                    curr = w
                else:
                    curr += w

            return needed_days <= days

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans