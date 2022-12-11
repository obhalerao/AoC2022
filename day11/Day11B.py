lines = [l.strip() for l in open("../input.txt").readlines()]

items = []

worries = []

monkeys = []

rules = []

nexts = []

operations = []

inspects = []

mod = 1

idx = 0
monkey = -1
for line in lines:
    if idx % 7 == 0:
        monkey+=1
        monkeys.append([])
        nexts.append([])
        inspects.append(0)
    elif idx % 7 == 1:
        l = line.split()
        l = l[2:]
        for val in l:
            monkeys[-1].append(len(items))
            items.append(monkey)
            if val[-1] == ',':
                worries.append(int(val[:-1]))
            else:
                worries.append(int(val))
    elif idx % 7 == 2:
        l = line.split()
        l = l[4:]
        if l[0] == '+':
            if l[1] == 'old':
                operations.append(("+", l[1]))
            else:
                z = int(l[1])
                operations.append(('+', int(l[1])))
        else:
            if l[1] == 'old':
                operations.append(("*", l[1]))
            else:
                z = int(l[1])
                operations.append(('*', int(l[1])))
    elif idx % 7 == 3:
        l = line.split()
        rules.append(int(l[-1]))
        mod*=int(l[-1])
    elif idx % 7 == 4 or idx % 7 == 5:
        l = line.split()
        nexts[-1].append(int(l[-1]))
    idx+=1

for round in range(10000):
    for i in range(len(monkeys)):
        while len(monkeys[i]) > 0:
            item = monkeys[i][0]
            if operations[i][0] == '+':
                if operations[i][1] == 'old':
                    worries[item] = worries[item]+worries[item]
                    worries[item]%=mod
                else:
                    worries[item] = worries[item]+operations[i][1]
                    worries[item]%=mod
            else:
                if operations[i][1] == 'old':
                    worries[item] = worries[item]*worries[item]
                    worries[item]%=mod
                else:
                    worries[item] = worries[item] * operations[i][1]
                    worries[item]%=mod
            inspects[i]+=1
            if worries[item] % rules[i] == 0:
                monkeys[nexts[i][0]].append(item)
            else:
                monkeys[nexts[i][1]].append(item)
            del monkeys[i][0]

inspects.sort()
print(inspects[-1]*inspects[-2])

