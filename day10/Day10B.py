lines = [l.strip() for l in open("../input.txt").readlines()]

val = 1
s = 0
idx = -1

image = [[' ' for i in range(40)] for j in range(6)]

valids = {val-1, val, val+1}

def draw(idx):
    global image, valids
    if idx % 40 in valids:
        image[idx // 40][idx % 40] = '#'
    else:
        image[idx // 40][idx % 40] = '.'

for line in lines:
    l = line.split()
    if l[0] == 'noop':
        idx+=1
        draw(idx)
    elif l[0] == 'addx':
        idx+=1
        draw(idx)
        idx+=1
        draw(idx)
        val+=int(l[1])
        valids = {val-1, val, val+1}

for i in image:
    print(''.join(i))