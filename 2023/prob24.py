cols, rows = map(int, input().split())
words = []
while True:
    w = input()
    if w == 'END': break
    words.append(w)

grid = [input() for _ in range(rows)]

def search(w):
    for i in range(rows):
        for j in range(cols):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    r, c = i, j
                    valid = True
                    for x in w:
                        if r < 0 or r >= rows or c < 0 or c >= cols or x != grid[r][c]:
                            valid = False
                            break
                        r, c = r + dr, c + dc
                    if valid: return True
    return False

found, missing = [], []
for w in words:
    if search(w):
        found.append(w)
    else:
        missing.append(w)
print(f"FOUND: {', '.join(sorted(found))}".strip())
print(f"MISSING: {', '.join(sorted(missing))}".strip())
