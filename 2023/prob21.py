def convert(x):
    return f"{((int)(x * 10)) / 10:.1f}"

d = float(input()) * 1000

arr = []
t = 0
while True:
    line = input()
    if line == "00": break
    name, data = line.split()
    dist = 0
    for x in data.split(";"):
        ab, v = x.split(":")
        v = float(v)
        start, t = map(int, ab.split("-"))
        dist += (t-start) * v
    arr.append((dist, len(arr), name))

place = [0] * len(arr)
arr.sort(reverse=True)
for finish_idx, (_, i, _) in enumerate(arr):
    place[i] = ["1st", "2nd", "3rd", "4th", "5th"][finish_idx]

arr.sort(key=lambda x: x[1])
for dist, i, name in arr:
    print(f"{name} {convert(dist)}m in {convert(t/60)}min ({place[i]})")
