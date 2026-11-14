class Solution:
    def encode(strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
    def decode(s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res