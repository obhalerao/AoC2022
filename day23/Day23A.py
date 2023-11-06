lines = [l for l in open("../input.txt").readlines()]

drs = [-1, 1, 0, 0, 1, -1, 1, -1]
dcs = [0, 0, -1, 1, 1, 1, -1, -1]

N = 0
S = 1
W = 2
E = 3
NE = 5
SE = 4
NW = 7
SW = 6

priority = [0, 1, 2, 3]

forbidden = [{0, 5, 7}, {1, 4, 6}, {2, 6, 7}, {3, 4, 5}]

grid = set()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '#':
            grid.add((r, c))

for round in range(10):
    proposals = {}
    ngrid = set()
    for elf in grid:
        r, c = elf
        exists = False
        for dr, dc in zip(drs, dcs):
            if (r+dr, c+dc) in grid:
                exists = True
        if exists:
            proposed = False
            for dir in priority:
                safe = True
                for ndir in forbidden[dir]:
                    nr, nc = r+drs[ndir], c+dcs[ndir]
                    if (nr, nc) in grid:
                        safe = False
                        break
                if safe:
                    nr, nc = r+drs[dir], c+dcs[dir]
                    if (nr, nc) not in proposals:
                        proposals[(nr, nc)] = []
                    proposals[(nr, nc)].append((r, c))
                    proposed = True
                    break
            if not proposed:
                ngrid.add(elf)
        else:
            ngrid.add(elf)

    for dest in proposals:
        if len(proposals[dest]) == 1:
            ngrid.add(dest)
        else:
            for elf in proposals[dest]:
                ngrid.add(elf)

    priority.append(priority[0])
    del priority[0]
    grid = ngrid

minr = float("inf")
maxr = float("-inf")
minc = float("inf")
maxc = float("-inf")

for elf in grid:
    minr = min(minr, elf[0])
    maxr = max(maxr, elf[0])
    minc = min(minc, elf[1])
    maxc = max(maxc, elf[1])

area = (maxr-minr+1)*(maxc-minc+1)

print(area-len(grid))