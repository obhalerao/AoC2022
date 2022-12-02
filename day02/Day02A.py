lines = [l.strip() for l in open("../input.txt").readlines()]

score = {'X': 1, 'Y':2, 'Z': 3}

s = 0
for line in lines:
    c1 = line.split()[0]
    c2 = line.split()[1]
    s+=score[c2]
    if c2 == 'Y' and c1 == 'A' or c2 == 'Z' and c1 == 'B' or c2 == 'X' and c1 == 'C':
        s+=6
    elif c2 == 'Y' and c1 == 'B' or c2 == 'X' and c1 == 'A' or c2 == 'Z' and c1 == 'C':
        s+=3
print(s)