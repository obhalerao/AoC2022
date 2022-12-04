lines = [l.strip() for l in open("../input.txt").readlines()]

cnt=0
for line in lines:
    a = line.split(',')
    a1,a2 = tuple(int(i) for i in a[0].split('-'))
    b1, b2 = tuple(int(i) for i in a[1].split('-'))
    if not(a1 < b1 and a2 < b1 or b1 < a1 and b2 < a1):
        cnt+=1
print(cnt)