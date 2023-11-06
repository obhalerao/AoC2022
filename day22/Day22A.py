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

r = 0
c = grid[0].index('.')
dir = 0

n = len(grid)
m = len(grid[0])

for instr in instructions:
    if isinstance(instr, int):
        for i in range(instr):
            nr = (r+dr[dir])%n
            nc = (c+dc[dir])%m
            while grid[nr][nc] == ' ':
                nr+=dr[dir]
                nr%=n
                nc+=dc[dir]
                nc%=m
            if grid[nr][nc] == '#':
                break
            r = nr
            c = nc
    else:
        if instr == 'R':
            dir+=1
            dir%=4
        else:
            dir-=1
            dir%=4

print(1000*(r+1)+4*(c+1)+dir)