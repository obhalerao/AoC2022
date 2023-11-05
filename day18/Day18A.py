lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[[False for i in range(50)] for j in range(50)] for k in range(50)]

for line in lines:
    a,b,c = tuple(int(i) for i in line.split(','))
    grid[a][b][c] = True

cnt = 0
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]


for i in range(50):
    for j in range(50):
        for k in range(50):
            if grid[i][j][k]:
                for x,y,z in zip(dx,dy,dz):
                    if not grid[i+x][j+y][k+z]:
                        cnt+=1
print(cnt)