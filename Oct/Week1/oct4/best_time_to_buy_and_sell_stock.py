class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        m = 0
        while r < len (prices) :
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > m :
                    m = profit
            else :
                l = r
            r +=1
        return m
        