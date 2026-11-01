class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            cur = res[0]
            count = 1
            new = ""
            for c in res[1:]:
                if c == cur:
                    count += 1
                else:
                    new = new + str(count) + cur
                    cur = c
                    count = 1
            res = new + str(count) + cur
        return res