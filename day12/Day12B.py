from collections import deque

lines = [l.strip() for l in open("../input.txt").readlines()]

grid = []

s = None
e = None

for idx, i in enumerate(lines):
    grid.append(list(i))
    for idx2, j in enumerate(grid[-1]):
        if j == 'S':
            s = (idx, idx2)
            grid[idx][idx2] = 'a'
        if j == 'E':
            e = (idx, idx2)
            grid[idx][idx2] = 'z'



q = deque()
dists = {}

for idx, i in enumerate(grid):
    for idx2, j in enumerate(i):
        if j == 'a':
            q.appendleft((idx, idx2))
            dists[(idx, idx2)] = 0

seen = set()
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

while q:
    tmp = q.pop()
    if tmp in seen:
        continue
    seen.add(tmp)
    for dx,dy in zip(dxs, dys):
        nc = (tmp[0]+dx, tmp[1]+dy)
        if nc[0] < 0 or nc[0] >= len(grid) or nc[1] < 0 or nc[1] >= len(grid[0]):
            continue
        if ord(grid[nc[0]][nc[1]]) > ord(grid[tmp[0]][tmp[1]])+1:
            continue
        if nc not in dists:
            dists[nc] = dists[tmp]+1
        else:
            dists[nc] = min(dists[nc], dists[tmp]+1)
        q.appendleft(nc)

print(dists[e])
