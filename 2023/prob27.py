n = int(input())

def increment(x):
    x += 1
    if x > n: x = 1
    return x

def decrement(x):
    x -= 1
    if x == 0: x = n
    return x

def decode(w, a, b, c):
    res = ''
    for x in w:
        if x.isalpha():
            idx = 26 - ((ord(x)-ord('A') +1 + a + b + c) % 26)
            res += chr(ord('A')-1+idx)
            if b % 3 == 0: a = increment(a)
            if c % 5 == 0: b = increment(b)
            c = increment(c)
        else:
            res += x
    return res

d = {}
for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            msg = decode("AMGINE", a, b, c)
            d[msg] = (a, b, c)

while True:
    w = input()
    if w == ".": break
    for msg in d:
        idx = w.find(msg)
        if idx >= 0:
            a, b, c = d[msg]
            while idx > 0:
                if w[idx].isalpha():
                    c = decrement(c)
                    if c % 5 == 0: b = decrement(b)
                    if b % 3 == 0: a = decrement(a)
                idx -= 1
            print(a, b, c)
            print(decode(w, a, b, c))
            break

