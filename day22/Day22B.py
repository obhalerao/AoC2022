lines = [l for l in open("../input.txt").readlines()]

lastline = lines[-1]

lines = [l[:-1] for l in lines][:-2]

instructions = []
lidx = 0
for i in range(len(lastline)):
    if lastline[i].isalpha():
        instructions.append(int(lastline[lidx:i]))
        instructions.append(lastline[i])
        lidx = i+1
instructions.append(int(lastline[lidx:]))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

grid = [list(i) for i in lines]
maxlen = max(len(i) for i in lines)
for idx in range(len(grid)):
    while len(grid[idx]) < maxlen:
        grid[idx].append(" ")

n = len(grid)
m = len(grid[0])

print(n, m)

nexts = [[[None for k in range(4)] for j in i] for i in grid]
for i in range(n):
    for j in range(m):
        if grid[i][j] == ' ':
            continue
        for dir in range(4):
            ni = (i+dr[dir])%n
            nj = (j+dc[dir])%m
            if grid[ni][nj] != ' ':
                nexts[i][j][dir] = (ni, nj, dir)

# fill in remainder of cube edges

for j in range(150, 200):
    nexts[j][49][0] = (149, j-100, 3)
    nexts[149][j-100][1] = (j, 49, 2)

for j in range(50):
    nexts[100][j][3] = (j+50, 50, 0)
    nexts[j+50][50][2] = (100, j, 1)

for j in range(100, 150):
    nexts[49][j][1] = (j-50, 99, 2)
    nexts[j-50][99][0] = (49, j, 3)

for j in range(50):
    nexts[j][149][0] = (149-j, 99, 2)
    nexts[149-j][99][0] = (j, 149, 2)

    nexts[j][50][2] = (149-j, 0, 0)
    nexts[149-j][0][2] = (j, 50, 0)

    nexts[199][j][1] = (0, j+100, 1)
    nexts[0][j+100][3] = (199, j, 3)

for j in range(150, 200):
    nexts[j][0][2] = (0, j-100, 1)
    nexts[0][j-100][3] = (j, 0, 0)

r = 0
c = grid[0].index('.')
dir = 0

for instr in instructions:
    if isinstance(instr, int):
        for i in range(instr):
            nr, nc, ndir = nexts[r][c][dir]
            if grid[nr][nc] == '#':
                break
            r = nr
            c = nc
            dir = ndir
    else:
        if instr == 'R':
            dir+=1
            dir%=4
        else:
            dir-=1
            dir%=4

print(r, c, dir)

print(1000*(r+1)+4*(c+1)+dir)