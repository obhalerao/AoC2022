import functools

lines = [l.strip() for l in open("../input.txt").readlines()]

def cmp(lst1, lst2):
    if type(lst1) == int and type(lst2) == int:
        return lst1-lst2
    else:
        if type(lst1) == int:
            lst1 = [lst1]
        if type(lst2) == int:
            lst2 = [lst2]
    for idx, i in enumerate(lst1):
        if idx >= len(lst2):
            return 1
        res = cmp(i, lst2[idx])
        if res != 0:
            return res
    if len(lst1) < len(lst2):
        return -1
    return 0

ii = 0
iii =0
def parse(str):
    global ii
    if str[ii] == '[':
        ii+=1
        res = []
        while str[ii] != ']':
            res.append(parse(str))
            if str[ii] == ']':
                break
            ii+=1
        ii+=1
        return res
    else:
        sk = ""
        while str[ii].isdigit():
            sk+=str[ii]
            ii+=1
        return int(sk)

cnt = 0

lidx = 0

lsts = []
while lidx < len(lines):
    ii=0
    l1 = parse(lines[lidx])
    lsts.append(l1)
    lidx+=1
    ii=0
    l2 = parse(lines[lidx])
    lsts.append(l2)
    lidx+=1
    lidx+=1

s1 = [[2]]

s2 = [[6]]

lsts.append(s1)
lsts.append(s2)

lsts.sort(key=functools.cmp_to_key(cmp))

print((lsts.index(s1)+1) * (lsts.index(s2)+1))