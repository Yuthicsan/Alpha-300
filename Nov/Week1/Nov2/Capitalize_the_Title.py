class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        ans = []
        for word in words:
            result = ""
            if len(word) <= 2:
                for ch in word:
                    if 65 <= ord(ch) <= 90:
                        result += chr(ord(ch)+32)
                    else:
                        result += ch                  
            else:
                for i in range(len(word)):
                    ch = word[i]
                    if i == 0:
                        if 97 <= ord(ch) <= 122:
                            result += chr(ord(ch) - 32)
                        else:
                            result += ch
                    else:
                        if 65 <= ord(ch) <= 90:
                            result += chr(ord(ch)+32)
                        else:
                            result += ch
            ans.append(result)
        return " ".join(ans)