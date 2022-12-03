lines = [l.strip() for l in open("../input.txt").readlines()]
s = 0
cs = set()
for idx, line in enumerate(lines):
    if len(cs) == 0:
        cs = set(list(line))
    else:
        cs = cs.intersection(set(list(line)))
        if idx % 3 == 2:
            for i in cs:
                print(i)
                if i.islower():
                    s += ord(i) - ord('a')
                else:
                    s += ord(i) - ord('A') + 26
            s+=1
            cs = set()


print(s)