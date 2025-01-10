### CodeWars XXVI - 30 - Escape the Fire

### Observation

* This is a shortest path problem, solvable using **Breadth First Search (BFS)** algorithm.
* The twist is that we have these valves on the empty rooms whose status (on or off) we will need to track.
* There can only be **at most 10 valves** in the grid (by the mention of the rooms on fire, `A .. J`).

### The Idea

*Note: If you haven't learned Breadth First Search (BFS), check this [Wikipedia article on BFS](https://en.wikipedia.org/wiki/Breadth-first_search) first.*

***Formulating the state*** of the BFS is key.  Usually on a grid setup like this, the state would just be the cell coordinates, namely *row* and *column*.  But this time, it won't be enough.  We will need to add another attribute as part of the state, that is, the on/off status of each valve.  This implies that during the BFS run, we *might visit the same cells more than once*, but every duplicate visit to that same cell will definitely have a **different on/off status of the valves**.  Since there can be at most 10 valves, this status can be viewed as a binary value with 10 bits, or a tuple with 10 values in it (0 or 1 for each), or a string like `"000101011"` where `'0'` and `'1'` is off and on, respectively.

The idea discussed here will be using bitwise operations.  You can convert it to a tuple or string based information to track which valves are on/off.  *Note: Do NOT use a list/array as part of your state because list/array is mutable and can't be part of a key of the dictionary, you'll get into bad situation if you do so.*

#### Starting State and Target State(s)
The *starting state* would then be `(r, c, m)` where `(r, c)` indicates the cell location of `'S'`, and `m` the starting state of all the valves, that is, 0 since all valves are off in the beginning.

We then run BFS algorithm to find the shortest path from the starting state to the *target state*, that is, any state which has an `'X'` on its cell position.

#### Moving from one state to another that is one-step-away from it
Suppose we are at state `(r, c, m)`.  Each movement costs 1 time unit and it will get us to the neighboring cells of `(r, c)`, that is: `(r-1, c)`, `(r+1, c)`, `(r, c-1)`, and `(r, c+1)`.

What about the 3<sup>rd</sup> attribute of the state, `m`?  In most cases, it will stay the same as the previous state.  The only time it will be different is when the neighbor we are trying to visit is the one that has the valve `'a' ..'j'`.  In such case, the next `m` value will be the current `m` plus the bit position of the corresponding valve set to 1.  For example, suppose that the current `m` value is `0b0000000010` (which indicates 2<sup>nd</sup> valve or valve `'b'` is on) and we are entering the neighbor with valve `'c'`, it means the the next `m` value will be OR-ed by the bit `0b0000000100` (that's the bitmask value for 3<sup>rd</sup> valve or valve `'c'`), giving us the value of `0b0000000110` (both valve 'b' and 'c' are on).  You can observe the bit positions that are set to 1 and we know those corresponding valves are already on.

However, it is possible that one or more of those *one-step-away* moves are invalid moves.  The key things to evaluate to see if we can get to the adjacent neighbor (in the code below, the next state is denoted by `(rr, cc, mm)`, that is, the state that is one step away from the current one being evaluated) are:
* See if the state is invalid because it either goes out of bounds, or it contains a wall `'#'`.
* If this next state is actually a valve room (`'a' .. 'j'`), then make sure we update the mask to indicate that the corresponding valve is on.
* If this next state is already seen/visited before, we should skip it.
* If this next state is a room on fire (`'A' .. 'J'`) and the corresponding valve to put out the fire is still off, then you have to skip since you can't get there yet.

Otherwise, add this newly found state to the queue.

Additionally, maintain a dictionary of to store the *previous state* of a known state.  This is useful to reconstruct back the shortest path we are taking.

```python
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
```
