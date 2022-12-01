lines = [l.strip() for l in open("../input.txt").readlines()]

mx = 0
cur = 0
tot = []
for line in lines:
    if(line == ''):
        tot.append(cur)
        cur=0
    else:
        cur+=int(line)
tot.sort()
print(tot[-1]+tot[-2]+tot[-3])