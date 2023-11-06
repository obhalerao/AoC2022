from collections import deque
from math import ceil

lines = [l.strip() for l in open("../input.txt").readlines()]

nds = {}
containsHuman = {}
result = {}

for line in lines:
    a = line.split(":")
    name = a[0]
    vals = a[1].split()
    if(len(vals) == 1):
        nds[name] = int(vals[0])
    else:
        if name == "root":
            nds[name] = (vals[0], "=", vals[2])
        else:
            nds[name] = (vals[0], vals[1], vals[2])

def parse(name):
    global nds, result
    if isinstance(nds[name], int):
        result[name] = nds[name]
        return nds[name]
    else:
        op = nds[name][1]
        left = parse(nds[name][0])
        right = parse(nds[name][2])
        result[name] = eval(str(left)+op+str(right))
        return result[name]

def containsHumn(name):
    global nds
    if name == "humn":
        containsHuman[name] = True
        return True
    if isinstance(nds[name], int):
        containsHuman[name] = False
        return False
    else:
        containsHuman[name] = containsHumn(nds[name][0]) or containsHumn(nds[name][2])
        return containsHuman[name]

target = 0
name = ""

if containsHumn(nds["root"][0]):
    target = parse(nds["root"][2])
    name = nds["root"][0]
else:
    target = parse(nds["root"][0])
    name = nds["root"][2]

while True:
    if name == "humn":
        print(target)
        break
    newname = ""
    first = False
    if containsHuman[nds[name][0]]:
        first = True
        parse(nds[name][2])
        ores = result[nds[name][2]]
        newname = nds[name][0]
    else:
        parse(nds[name][0])
        ores = result[nds[name][0]]
        newname = nds[name][2]
    if nds[name][1] == "+":
        target-=ores
    elif nds[name][1] == "-":
        if first:
            target+=ores
        else:
            target = -(target-ores)
    elif nds[name][1] == "*":
        target/=ores
    else:
        if first:
            target*=ores
        else:
            target = 1.0/(target/ores)

    name = newname


