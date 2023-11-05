lines = [l.strip() for l in open("../input.txt").readlines()]

board = [['.' for j in range(7)] for i in range(1000000)]
rock1 = ['####']
rock2 = ['.#.','###','.#.']
rock3 = ['..#','..#','###']
rock4 = ['#','#','#','#']
rock5 = ['##','##']
rocks = [rock1,rock2,rock3,rock4,rock5]
jets = lines[0]

highest = 0
heights = [0 for i in range(7)]
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

def updateHeights(r, c):
    global board, heights, rockidx, rocks
    rock = rocks[rockidx]
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if (board[r+i][c+j] == '@'):
                heights[c+j] = max(heights[c+j], len(board)-(r+i)-1)



def process():
    global board, rocks, rockidx, jets, jetidx, rockcnt, highest
    rock = rocks[rockidx]
    r = (1000000 - highest - 3 - len(rock))
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
    updateHeights(r, c)
    rockcnt+=1
    rockidx = (rockidx + 1) % len(rocks)
    highest = max(highest, (1000000-r))
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if(rock[i][j] != '.'):
                board[r+i][c+j] = '#'

def computeState():
    global board, heights, jetidx, rockidx
    nheights = heights.copy()
    minh = min(nheights)
    for i in range(len(nheights)):
        nheights[i]-=minh
    return (tuple(nheights), jetidx, rockidx)


num = 1000000000000

states = {}

cyclelen = 0
oiter = 0
enditer = 0
ht = 0


sts = []

for i in range(num):
    process()
    state = computeState()
    if state in states:
        print(state)
        oiter = states[state]
        cyclelen = i-oiter
        enditer = i
        print(oiter)
        print(cyclelen)
        ht = highest
        break
    states[state] = i
    sts.append(state)

oh = highest

for i in range(cyclelen):
    process()

ht = highest-oh

idxx = enditer+cyclelen

iters = (num-idxx) // cyclelen
ht*=(iters+1)
numleft = (num-idxx) % cyclelen
oh2 = highest
for i in range(numleft):
    process()
print(oh+ht+(highest-oh2)-1)

# print(cyclelen)
# oh = ht
# ht*=iters
# numleft = num % cyclelen
# for i in range(numleft):
#     process()
# print(ht+(highest-oh))











