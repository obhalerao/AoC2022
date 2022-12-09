lines = [l.strip() for l in open("../input.txt").readlines()]

def valid(head, tail):
    return abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1

def next(head, tail):
    if not valid(head, tail):
        return tail
    if head[0] == tail[0]:
        if head[1]-2 == tail[1]:
            return (tail[0], tail[1]+1)
        else:
            return (tail[0], tail[1]-1)
    elif head[1] == tail[1]:
        if head[0]-2 == tail[0]:
            return (tail[0]+1, tail[1])
        else:
            return (tail[0]-1, tail[1])
    else:
        if head[0]-tail[0] <= -1 and head[1]-tail[1] <= -1:
            return (tail[0]-1, tail[1]-1)
        if head[0]-tail[0] >= 1 and head[1]-tail[1] <= -1:
            return (tail[0]+1, tail[1]-1)
        if head[0]-tail[0] >= 1 and head[1]-tail[1] >= 1:
            return (tail[0]+1, tail[1]+1)
        if head[0]-tail[0] <= -1 and head[1]-tail[1] >= 1:
            return (tail[0]-1, tail[1]+1)
    return (float("-inf"), float("-inf"))




knots = [(0,0) for i in range(10)]

seen = set()
seen.add(knots[-1])

for line in lines:
    l = line.split()
    dir = l[0]
    mov = int(l[1])
    for i in range(mov):
        if dir == 'R':
            knots[0] = (knots[0][0]+1, knots[0][1])
            for q in range(9):
                knots[q+1] = next(knots[q], knots[q+1])
        if dir == 'L':
            knots[0] = (knots[0][0] - 1, knots[0][1])
            for q in range(9):
                knots[q + 1] = next(knots[q], knots[q+1])
        if dir == 'U':
            knots[0] = (knots[0][0], knots[0][1]+1)
            for q in range(9):
                knots[q + 1] = next(knots[q], knots[q + 1])
        if dir == 'D':
            knots[0] = (knots[0][0], knots[0][1] - 1)
            for q in range(9):
                knots[q + 1] = next(knots[q], knots[q + 1])
        seen.add(knots[-1])

print(len(seen))
