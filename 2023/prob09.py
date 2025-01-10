n = int(input())
t = int(input())
for _ in range(n):
    v, car = map(lambda x: int(x) if x.isdigit() else x, input().split())
    d = int(v * 5 * t / 3)
    print(f"({d/100:.2f})", end="")
    print(f"{'-' * (d // 500)}", end="")
    d %= 500
    print(f"{'~' * (d//100)}", end="")
    d %= 100
    print("{}" * (d // 25), end="")
    print(car)