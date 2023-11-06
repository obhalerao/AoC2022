from collections import deque
from math import ceil

lines = [l.strip() for l in open("../input.txt").readlines()]

nds = {}

for line in lines:
    a = line.split(":")
    name = a[0]
    vals = a[1].split()
    if(len(vals) == 1):
        nds[name] = int(vals[0])
    else:
        nds[name] = (vals[0], vals[1], vals[2])

def parse(name):
    global nds
    if isinstance(nds[name], int):
        return nds[name]
    else:
        op = nds[name][1]
        left = parse(nds[name][0])
        right = parse(nds[name][2])
        return eval(str(left)+op+str(right))

print(parse("root"))

