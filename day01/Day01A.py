lines = [l.strip() for l in open("../input.txt").readlines()]

mx = 0
cur = 0
for line in lines:
    if(line == ''):
        mx = max(cur, mx)
        cur=0
    else:
        cur+=int(line)
print(mx)