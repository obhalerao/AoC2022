from collections import deque

lines = [l.strip() for l in open("../input.txt").readlines()]

drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

dirs_map = {'^' : 0, '>' : 1, 'v' : 2, '<' : 3}

n = len(lines)
m = len(lines[0])

start = (0, 1)
end = (n-1, m-2)

rmod = n-2
cmod = m-2

# blizzard: (start_r, start_c, direction)

blizzards = set()

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char in dirs_map:
            blizzards.add((r, c, dirs_map[char]))

def check_blizzard(time, r, c):
    global blizzards, rmod, cmod
    # north
    nr = r
    nc = c
    nr-=1
    nr-=time
    nr%=rmod
    nr+=1
    if (nr, nc, 2) in blizzards:
        return True

    # south

    nr = r
    nc = c
    nr -= 1
    nr += time
    nr %= rmod
    nr += 1
    if (nr, nc, 0) in blizzards:
        return True

    # east

    nr = r
    nc = c
    nc -= 1
    nc += time
    nc %= cmod
    nc +=1
    if (nr, nc, 3) in blizzards:
        return True

    # west
    nr = r
    nc = c
    nc -= 1
    nc -= time
    nc %= cmod
    nc += 1
    if (nr, nc, 1) in blizzards:
        return True

    return False


q = deque()

# deque state: r, c, time

q.append((0, 1, 0))

seen = set()
par = {}

finalstate = None

while q:
    r, c, time = q.popleft()
    if (r, c) == end:
        finalstate = (r, c, time)
        print(time)
        break
    if time > 3*(n+m)*(n+m):
        continue
    if (r, c, time) in seen:
        continue
    seen.add((r, c, time))
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if lines[nr][nc] == '#':
            continue
        if not check_blizzard(time+1, nr, nc):
            q.append((nr, nc, time+1))
    if not check_blizzard(time+1, r, c):
        q.append((r, c, time+1))




