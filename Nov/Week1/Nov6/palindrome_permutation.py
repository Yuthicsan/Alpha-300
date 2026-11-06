def find_permutation(self, st):
    st = st.lower()
    d = {}
    for char in st:
        if char == ' ':
            continue
        if char in d:
            d[char] += 1
        else:
            # Simplified check for character range (a-z)
            if ord(char) >= 97 and ord(char) <= 122:
                d[char] = 1
    
    middle = False
    for char in d:
        if middle and d[char] % 2 == 1:
            return False
        elif d[char] % 2 == 1:
            middle = True
    return True 