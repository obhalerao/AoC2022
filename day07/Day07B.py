lines = [l.strip() for l in open("../input.txt").readlines()]

directories = {'/':[]}
sizes = {'/':-1}
files = set()

stk = []

for line in lines:
    ls = line.split()
    curdir = '/'.join(stk)
    if ls[0] == 'dir':
        directories['/'.join(stk)+'/'+ls[1]] = []
        sizes['/'.join(stk)+'/'+ls[1]] = -1
        directories[curdir].append(ls[1])
    elif ls[0] == '$' and ls[1] == 'cd':
        if ls[2] == '..':
            stk.pop()
        else:
            stk.append(ls[2])
    elif ls[0] != '$':
        sizes['/'.join(stk)+'/'+ls[1]] = int(ls[0])
        files.add('/'.join(stk)+'/'+ls[1])
        directories[curdir].append(ls[1])

stk = ['/']
def dfs(node):
    global directories, sizes
    if sizes['/'.join(stk)] >= 0:
        return sizes['/'.join(stk)]
    s = 0
    for i in directories['/'.join(stk)]:
        stk.append(i)
        s+=dfs(i)
        stk.pop()
    sizes['/'.join(stk)] = s
    return s

dfs('/')
ss = 0

unused = 70000000 - sizes['/']
unused = 30000000 - unused

print(unused)

ans = float("inf")
for i in sizes:
    if i not in files and sizes[i] >= unused:
        ans = min(ans, sizes[i])
print(ans)