lines = [l.strip() for l in open("../input.txt").readlines()]

arr = []
for i in lines:
    arr.append([])
    for j in i:
        arr[-1].append(int(j))

cnt = 0
vis = [[False for i in range(len(arr[0]))] for j in range(len(arr))]
print(arr)
for i in range(len(arr)):
    mx = 0
    for j in range(len(arr[0])):
        if j == 0 or arr[i][j] > mx:
            mx = arr[i][j]
            vis[i][j] = True

print(vis)

for i in range(len(arr)):
    mx = 0
    for j in range(len(arr[0])-1, -1, -1):
        if j == len(arr[0])-1 or arr[i][j] > mx:
            mx = arr[i][j]
            vis[i][j] = True


for j in range(len(arr[0])):
    mx=0
    for i in range(len(arr)):
        if i == 0 or arr[i][j] > mx:
            mx = arr[i][j]
            vis[i][j] = True




for j in range(len(arr[0])):
    mx=0
    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1 or arr[i][j] > mx:
            mx = arr[i][j]
            vis[i][j] = True




print(sum(sum(i for i in j) for j in vis))

