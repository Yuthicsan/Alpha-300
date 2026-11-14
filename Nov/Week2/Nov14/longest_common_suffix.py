def longestCommonSuffix(strs: list[str]) -> str:
    if not strs:
        return ""
    base = strs[0]
    n = len(base)
    for i in range(1, n + 1):
        char = base[-i]
        for s in strs[1:]:
            if i > len(s) or s[-i] != char:
                return base[n - i + 1:]
                
    return base