a = int(input())
n = int(input())
p = 0
while True:
    if a ** p == n:
        print(f"{a}^{p} = {n}")
        break
    p += 1
