N = 36
t = [0] * N
t[1], t[2] = 1, 1
for i in range(3, N): t[i] = t[i-1] + t[i-2] + t[i-3]

for a, b in (map(int, line.split()) for line in open(0)):
    if a == 0 and b == 0: break
    print(abs(t[a]-t[b]))
