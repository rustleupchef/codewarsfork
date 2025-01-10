from itertools import permutations

n = int(input())
grid = [[x for x in input()] for _ in range(n)]

def solution(p):
    for i, j in enumerate(p):
        grid[i][j] = grid[i][j].upper()
        print(''.join(grid[i]))

for p in permutations(range(n)):
    valid = True
    gardens = set()
    for i, j in enumerate(p):
        if i+1 < n and abs(j-p[i+1]) == 1: valid = False
        gardens.add(grid[i][j])
    if valid and len(gardens) == n:
        solution(p)
        break
