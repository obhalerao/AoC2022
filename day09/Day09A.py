lines = [l.strip() for l in open("../input.txt").readlines()]

def valid(head, tail, idx):
    return abs(head[idx]-tail[idx]) > 1

head = (0,0)
tail = (0,0)

seen = set()
seen.add(tail)

for line in lines:
    l = line.split()
    dir = l[0]
    mov = int(l[1])
    for i in range(mov):
        if dir == 'R':
            head = (head[0]+1, head[1])
            if valid(head, tail, 0):
                tail = (head[0]-1, head[1])
        if dir == 'L':
            head = (head[0]-1, head[1])
            if valid(head, tail, 0):
                tail = (head[0]+1, head[1])
        if dir == 'U':
            head = (head[0], head[1]+1)
            if valid(head, tail, 1):
                tail = (head[0], head[1]-1)
        if dir == 'D':
            head = (head[0], head[1]-1)
            if valid(head, tail, 1):
                tail = (head[0], head[1]+1)
        seen.add(tail)

print(len(seen))
