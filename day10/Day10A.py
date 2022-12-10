lines = [l.strip() for l in open("../input.txt").readlines()]

val = 1
s = 0
idx = -1
for line in lines:
    l = line.split()
    if l[0] == 'noop':
        idx+=1
        if idx+1 == 20 or idx+1 == 60 or idx+1==100 or idx+1==140 or idx+1==180 or idx+1==220:
            s+=(idx+1)*val
    elif l[0] == 'addx':
        idx+=1
        if idx+1 == 20 or idx+1 == 60 or idx+1==100 or idx+1==140 or idx+1==180 or idx+1==220:
            s+=(idx+1)*val
        idx+=1
        if idx+1 == 20 or idx+1 == 60 or idx+1==100 or idx+1==140 or idx+1==180 or idx+1==220:
            s+=(idx+1)*val
        val+=int(l[1])

print(s)