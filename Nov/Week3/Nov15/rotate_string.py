class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double_s = s + s
        n = len(double_s)
        m = len(goal)
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if double_s[i + j] != goal[j]:
                    match = False
                    break
            if match:
                return True
        return False