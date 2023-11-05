from collections import deque

lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[[False for i in range(50)] for j in range(50)] for k in range(50)]

for line in lines:
    a,b,c = tuple(int(i) for i in line.split(','))
    grid[a][b][c] = True


steam = [[[False for i in range(50)] for j in range(50)] for k in range(50)]

# do bfs or smth
cnt = 0
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

q = deque()
q.append((0,0,0))
while q:
    a,b,c = q.popleft()
    if steam[a][b][c]:
        continue
    steam[a][b][c] = True
    for x,y,z in zip(dx,dy,dz):
        if a+x >= 0 and a+x < 50 and b+y >= 0 and b+y < 50 and c+z >= 0 and c+z < 50 and not grid[a+x][b+y][c+z]:
            q.append((a+x,b+y,c+z))

for i in range(50):
    for j in range(50):
        for k in range(50):
            if grid[i][j][k]:
                for x,y,z in zip(dx,dy,dz):
                    if steam[i+x][j+y][k+z]:
                        cnt+=1
print(cnt)