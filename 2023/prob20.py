value = int(input())
m, last = 512, 0
res = []
while m:
    if value & m:
        print(f"{m}=1")
        if last:
            res.append(f"{last}+{m} = {last+m}")
        last += m
    else:
        print(f"{m}=0")
    m = m >> 1
for x in res: print(x)
print(f"{last} = {bin(value)[2:]}")
