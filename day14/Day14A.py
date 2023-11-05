lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [['.' for i in range(1000)] for j in range(1000)]

def simulate():
    global grid
    r = 500
    c = 0
    try:
        while True:
            if grid[r][c+1] == '.':
                c+=1
            elif grid[r-1][c+1] == '.':
                r-=1
                c+=1
            elif grid[r+1][c+1] == '.':
                r+=1
                c+=1
            else:
                break
    except:
        return False
    grid[r][c] = '#'
    return True

for line in lines:
    lst = line.split(' -> ')
    coords = []
    for coord in lst:
        coords.append(tuple(int(i) for i in coord.split(',')))
    r = coords[0][0]
    c = coords[0][1]
    for i in range(1, len(coords)):
        while True:
            grid[r][c] = '#'
            if r < coords[i][0]:
                r+=1
            elif r > coords[i][0]:
                r-=1
            elif c < coords[i][1]:
                c+=1
            elif c > coords[i][1]:
                c-=1
            else:
                break

cnt = 0
while simulate():
    cnt+=1

print(cnt)

