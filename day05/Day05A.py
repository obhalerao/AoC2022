from collections import deque

lines = [l.rstrip() for l in open("../input.txt").readlines()]

idx = 0
nlines = []
while lines[idx] != '':
    nlines.append(lines[idx])
    idx+=1

nlines.reverse()
n = 0
stacks = []
for idx1, line in enumerate(nlines):
    if idx1 == 0:
        n = int(line.split()[-1])
        stacks = [deque() for i in range(n)]
    else:
        cnt = 0
        idxx=0
        while idxx < len(line):
            if line[idxx+1].isalpha():
                stacks[cnt].append(line[idxx+1])
            idxx+=4
            cnt+=1

idx+=1
while idx < len(lines):
    line = lines[idx].split()
    a = int(line[1])
    b = int(line[3])-1
    c = int(line[5])-1
    for i in range(a):
        x = stacks[b].pop()
        stacks[c].append(x)
    idx+=1

print(''.join(i[-1] for i in stacks))
