class Solution:
    def checkString(self, s: str) -> int:
        count = 0
        for ch in s:
            if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
                count += 1
            elif ord(ch) >= 97 and ord(ch) <= 122:
                count-=1
        if count < 0:
            return -1
        elif count == 0:
            return 0
        else:
            return 1