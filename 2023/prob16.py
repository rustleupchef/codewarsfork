def modify(word, a, b):
    res = ''
    for x in word.upper():
        if x == a:
            res += b
        elif x == b:
            res += a
        else:
            res += x
    return res

a, b = input().split()
arr = []
while True:
    word = input()
    if word == "END": break
    arr.append((modify(word, a, b), word))

for _, w in sorted(arr):
    print(w)
