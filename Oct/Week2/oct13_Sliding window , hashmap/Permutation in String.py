class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for c in s1:
            cnt1[ord(c) - ord('a')] += 1

        k = len(s1)

        for i in range(len(s2)):
            cnt2[ord(s2[i]) - ord('a')] += 1

            if i >= k:
                cnt2[ord(s2[i - k]) - ord('a')] -= 1

            if cnt1 == cnt2:
                return True

        return False
