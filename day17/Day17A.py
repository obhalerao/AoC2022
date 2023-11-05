lines = [l.strip() for l in open("../input.txt").readlines()]

board = [['.' for j in range(7)] for i in range(10000)]
rock1 = ['####']
rock2 = ['.#.','###','.#.']
rock3 = ['..#','..#','###']
rock4 = ['#','#','#','#']
rock5 = ['##','##']
rocks = [rock1,rock2,rock3,rock4,rock5]
jets = lines[0]

highest = 0
rockcnt = 0
rockidx = 0
jetidx = 0

def move(r, c, left=False, right=False, down=False):
    global rocks,rockidx, board
    rock = rocks[rockidx]
    nr = r
    nc = c
    if(left and not touchingLeft(r, c)):
        nc-=1
    if(right and not touchingRight(r, c)):
        nc+=1
    if(down):
        nr+=1
    for i in range(len(rock)):
        for j in range(len(rock[i])):
            if(board[r+i][j+c] == '@'):
                board[r+i][j+c] = '.'
    for i in range(len(rock)):
        for j in range(len(rock[i])):
            if(rock[i][j] == '#'):
                board[nr+i][j+nc] = '@'
    return (nr, nc)

def touchingLeft(r, c):
    global board, rocks, rockidx
    rock = rocks[rockidx]
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if (c+j == 0 and board[r+i][c+j] == '@') or (c+j > 0 and board[r+i][c+j] == '@' and board[r+i][c+j-1] == '#'):
                return True
    return False

def touchingRight(r, c):
    global board, rocks, rockidx
    rock = rocks[rockidx]
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if (c+j == len(board[0])-1 and board[r+i][c+j] == '@') or (c+j < len(board[0])-1 and board[r+i][c+j] == '@' and board[r+i][c+j+1] == '#'):
                return True
    return False

def touchingDown(r, c):
    global board, rocks, rockidx
    rock = rocks[rockidx]
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if (r+i == len(board)-1 and board[r+i][c+j] == '@') or (r+i < len(board)-1 and board[r+i][c+j] == '@' and board[r+i+1][c+j] == '#'):
                return True
    return False


def process():
    global board, rocks, rockidx, jets, jetidx, rockcnt, highest
    rock = rocks[rockidx]
    r = (10000 - highest - 3 - len(rock))
    c = 2
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if(rock[i][j] != '.'):
                board[r+i][c+j] = '@'
    while True:
        if jets[jetidx] == '<':
            r,c = move(r, c, left=True)
        else:
            r,c = move(r, c, right=True)
        jetidx = (jetidx+1) % len(jets)
        if(touchingDown(r, c)):
            break
        r,c = move(r, c, down=True)
    rockcnt+=1
    rockidx = (rockidx + 1) % len(rocks)
    highest = max(highest, (10000-r))
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if(rock[i][j] != '.'):
                board[r+i][c+j] = '#'

for i in range(2022):
    process()

print(highest)


