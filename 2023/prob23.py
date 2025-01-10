line = input()
for _ in range(3): input()
d = {}
for sub_info in input().split(";"):
    key, letters = sub_info.lower().split(":")
    d[key] = letters.split(",")

vocab = set()
while True:
    w = input()
    if w == 'ZZZZZ': break
    vocab.add(w)

def correct(w):
    if w in vocab: return w
    for i, x in enumerate(w):
        for y in d[x]:
            ww = w[:i] + y + w[i+1:]
            if ww in vocab: return ww
    return w

print(' '.join(map(correct, line.split(" "))))