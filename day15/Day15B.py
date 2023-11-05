lines = [l.strip() for l in open("../input.txt").readlines()]

def merge(i1, i2):
    if i1[1] < i2[0]-1:
        return None
    elif i1[1] >= i2[1]:
        return i1
    else:
        return (i1[0], i2[1])

beacons = {}

beaconset = set()

for line in lines:
    ls = line.split()
    x1 = int(ls[2][2:-1])
    y1 = int(ls[3][2:-1])
    x2 = int(ls[8][2:-1])
    y2 = int(ls[9][2:])
    beacons[(x1, y1)] = (x2, y2)
    beaconset.add((x2, y2))

for row in range(3200000, 4000001):
    if row % 100000 == 0:
        print(row)
    intervals = []
    for sensor in beacons:
        dist = abs(sensor[0]-beacons[sensor][0])+abs(sensor[1]-beacons[sensor][1])
        length = max(-1, dist-abs((sensor[1]-row)))
        if length < 0:
            continue
        else:
            intervals.append((sensor[0]-length, sensor[0]+length))
    if len(intervals) == 0:
        continue
    intervals.sort()
    nintervals = []
    nintervals.append(intervals[0])
    for i in range(1, len(intervals)):
        val = merge(nintervals[-1], intervals[i])
        if not val:
            nintervals.append(intervals[i])
        else:
            nintervals.pop()
            nintervals.append(val)

    if len(nintervals) > 1:
        print(row, nintervals, (nintervals[0][1]+1)*4000000+row)
        break