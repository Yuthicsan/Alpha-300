s = "aaaba"
total = 0
run_len = 0
for i in range(len(s)):
    if i > 0 and s[i] == s[i - 1]:
        run_len += 1
    else:
        run_len = 1
    total += run_len
print(total)