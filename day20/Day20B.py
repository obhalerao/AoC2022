from collections import deque
from math import ceil

key = 811589153

arr_cpy = [(int(l.strip())*key, idx) for idx, l in enumerate(open("../input.txt").readlines())]
arr = [i for i in arr_cpy]

n = len(arr)



for num_times in range(10):
    indices = {}
    for idx, i in enumerate(arr):
        indices[i] = idx
    for idx, i in enumerate(arr_cpy):
        diff = i[0]%(n-1)
        curidx = indices[i]
        for j in range(abs(diff)):
            if diff > 0:
                curidx+=1
                curidx%=n
                tmp = arr[curidx]
                indices[tmp] = (curidx-1)%n
                arr[(curidx-1)%n] = tmp
            else:
                curidx-=1
                curidx%=n
                tmp = arr[curidx]
                indices[tmp] = (curidx+1)%n
                arr[(curidx+1)%n] = tmp
            arr[curidx] = i
            indices[i] = curidx
    print(f"done mixing {num_times+1} times")

zidx = 0
for idx, i in enumerate(arr):
    if i[0] == 0:
        zidx = idx
        break

print(arr[(1000+zidx)%n][0]+arr[(2000+zidx)%n][0]+arr[(3000+zidx)%n][0])
