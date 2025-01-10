rows, cols = map(int, input().split())
grid = [[x for x in input()] for _ in range(rows)]

def solution(r, c, m, pred):
    res = []
    while True:
        if grid[r][c].isalpha(): res.append(grid[r][c])
        if pred[(r, c, m)] is None: break
        r, c, m = pred[(r, c, m)]
    print(' '.join(res[::-1]))
    return True

def bit_for_valve(ch):
    return 1 << (ord(ch)-ord('a'))

def bit_for_fire(ch):
    return 1 << (ord(ch)-ord('A'))

def is_fire(r, c):
    return 'A' <= grid[r][c] <= 'J'

def is_valve(r, c):
    return 'a' <= grid[r][c] <= 'j'

def bfs(r, c, m):
    q, pred = [(r, c, m)], {(r, c, m): None}
    i = 0
    while i < len(q):
        r, c, m = q[i]
        i += 1

        if grid[r][c] == 'X':
            return solution(r, c, m, pred)

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rr, cc, mm = r + dr, c + dc, m
            if rr < 0 or rr >= rows or cc < 0 or cc >= cols: continue                   # out of bounds
            if grid[rr][cc] == '#': continue                                            # impassable wall
            if is_valve(rr, cc):
                mm |= bit_for_valve(grid[rr][cc])
            if (rr, cc, mm) in pred: continue                                           # already seen this state
            if is_fire(rr, cc) and (mm & bit_for_fire(grid[rr][cc])) == 0: continue     # can't get into fire without valve

            q.append((rr, cc, mm))
            pred[(rr, cc, mm)] = (r, c, m)
    return False

for i in range(rows):
    if 'S' in grid[i]:
        bfs(i, grid[i].index('S'), 0)
        break

            