class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        current = ""
        for word in words:
            current += word
            if current == s:
                return True
            if len(current) > len(s):
                break
                
        return False