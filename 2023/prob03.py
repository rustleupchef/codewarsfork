n = int(input())
c = int(input())
r = float(input())
t = int(input())

p = int(n * (1 + r) * t)
print(f"At the current rate of growth there will be {p} ponies in {t} years.")
if p > c:
    print(f"Celestia will need to add space for at least {p-c} ponies!")
else:
    print("Celestia won't need to add space yet!")
