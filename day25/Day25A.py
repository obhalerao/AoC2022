from collections import deque

lines = [l.strip() for l in open("../input.txt").readlines()]

sm = 0

for line in lines:
    base = 1
    cur = 0
    for x in line[::-1]:
        if x == '-':
            cur-=base
        elif x == '=':
            cur-=(2*base)
        else:
            cur+=(base*(int(x)))
        base*=5
    sm+=cur

ans = []
while sm != 0:
    val = sm % 5
    if val == 3:
        ans.append('=')
    elif val == 4:
        ans.append('-')
    else: ans.append(str(val))
    if val <= 2:
        sm-=val
    else:
        sm+=(5-val)
    sm//=5
print(''.join(reversed(ans)))


