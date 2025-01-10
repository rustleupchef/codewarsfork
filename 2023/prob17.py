s = input()
n = len(s)
len_limit = n // 3
for l in range(1, len_limit+1):
    pattern = s[:l]
    expected = n // l
    for i in range(1, expected):
        if s[l*i:l*(i+1)] != pattern: break
    else:
        if pattern.startswith(s[expected*l:]):
            rem = l - (n % l)
            print(pattern[-rem:])
            print(pattern)
            break