cache = {}

def solve(n):
    if n in cache: return cache[n]
    f = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            other = n // d
            if other > d:
                f.append(other)
        d += 1
    f.sort(reverse=True)

    res = [[n]]
    for d in f:
        for next_arr in solve(n // d):
            if any(map(lambda x: x > d, next_arr)): continue
            arr = [d]
            arr.extend(next_arr)
            res.append(arr)

    cache[n] = res
    return res

def get_factors(arr):
    return f"({'*'.join(map(str, arr))})"

def solution(n, res):
    print(f"{n}=", end="")
    print(','.join(map(get_factors, res)))

for line in open(0):
    n = int(line)
    if n == 0: break
    res = solve(n)
    if len(res) > 1:
        solution(n, res[1:])