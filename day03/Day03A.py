lines = [l.strip() for l in open("../input.txt").readlines()]
s = 0
for line in lines:
    l = len(line)
    first = line[:l//2]
    last = line[l//2:]
    a = set(list(first))
    b = set(list(last))
    inte = a.intersection(b)
    for i in inte:
        print(i)
        if i.islower():
            s+=ord(i)-ord('a')
        else:
            s+=ord(i)-ord('A')+26
    s+=1

print(s)