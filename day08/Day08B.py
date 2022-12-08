lines = [l.strip() for l in open("../input.txt").readlines()]

arr = []
for i in lines:
    arr.append([])
    for j in i:
        arr[-1].append(int(j))

cnt = 0
scores = [[1 for i in range(len(arr[0]))] for j in range(len(arr))]



for i in range(len(arr)):
    indices = [0 for p in range(10)]
    mx = 0
    for j in range(len(arr[0])):
        mi = float("-inf")
        for k in range(arr[i][j], 10):
            mi=max(mi, indices[k])
        scores[i][j]*=(j-mi)
        indices[arr[i][j]] = j

for i in range(len(arr)):
    indices = [0 for p in range(10)]
    mx = 0
    for j in range(len(arr[0])-1, -1, -1):
        mi = float("-inf")
        for k in range(arr[i][j], 10):
            mi = max(mi, indices[k])
        scores[i][j] *= ((len(arr[0])-j-1) - mi)
        indices[arr[i][j]] = len(arr[0])-j-1


for j in range(len(arr[0])):
    indices = [0 for i in range(10)]
    for i in range(len(arr)):
        mi = float("-inf")
        for k in range(arr[i][j], 10):
            mi = max(mi, indices[k])
        scores[i][j] *= (i - mi)
        indices[arr[i][j]] = i




for j in range(len(arr[0])):
    indices = [0 for i in range(10)]
    mx=0
    for i in range(len(arr)-1, -1, -1):
        mi = float("-inf")
        for k in range(arr[i][j], 10):
            mi = max(mi, indices[k])
        scores[i][j] *= ((len(arr) - i - 1) - mi)
        indices[arr[i][j]] = len(arr)-i-1

print(scores)

print(max(max(i for i in j) for j in scores))