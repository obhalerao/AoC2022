lines = [l.strip() for l in open("../input.txt").readlines()]

score = {'X': 1, 'Y':2, 'Z': 3}

s = 0
for line in lines:
    c1 = line.split()[0]
    c2 = line.split()[1]
    if c2 == 'Y':
        s+=3
    if c2 == 'Z':
        s+=6
    if c1 == 'A':
        if c2 == 'X':
            s+=3
        elif c2 == 'Y':
            s+=1
        else:
            s+=2
    elif c1 == 'B':
        if c2 == 'X':
            s+=1
        elif c2 == 'Y':
            s+=2
        else:
            s+=3
    else:
        if c2 == 'X':
            s+=2
        elif c2 == 'Y':
            s+=3
        else:
            s+=1

print(s)