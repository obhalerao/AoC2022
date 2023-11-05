lines = [l.strip() for l in open("../input.txt").readlines()]

dists = {}

rates = {}

edges = {}

for line in lines:
    ls = line.split()
    cur_valve = ls[1]
    edges[cur_valve] = []
    dists[cur_valve] = {}
    rate = int(ls[4].split('=')[-1][:-1])
    rates[cur_valve] = rate
    for nxt in ls[9:]:
        nnxt = nxt
        if nxt[-1] == ',':
            nnxt = nxt[:-1]
        edges[cur_valve].append(nnxt)
        dists[cur_valve][nnxt] = 1
    dists[cur_valve][cur_valve] = 0

for i in dists:
    for j in dists:
        if j not in dists[i]:
            dists[i][j] = float("inf")

for k in dists:
    for i in dists:
        for j in dists:
            if dists[i][j] > dists[i][k] + dists[k][j]:
                dists[i][j] = dists[i][k] + dists[k][j]

relevant = ['AA']
for idx in rates:
    if rates[idx] > 0:
        relevant.append(idx)

relset = set(relevant)

invrelevant = {i:idx for idx, i in enumerate(relevant)}

dp = [[[float("-inf") for k in range(len(relevant))] for j in range(1 << len(relevant))] for i in range(31)]
dp[0][1][0] = 0

for i in range(31):
    print(i)
    for j in range(1 << len(relevant)):
        tot = 0
        for k in range(len(relevant)):
            if j & (1 << k) > 0:
                tot+=rates[relevant[k]]
        for k in range(len(relevant)):
            dp[30][j][k] = max(dp[30][j][k], dp[i][j][k]+(30-i)*tot)
            for nxt in relevant:
                inxt = invrelevant[nxt]
                if(j & (1 << inxt) != 0):
                    continue
                dst = dists[relevant[k]][nxt]+1
                if i + dst <= 30:
                    nval = dp[i][j][k]+dst*tot
                    dp[i+dst][j | (1 << inxt)][inxt] = max(dp[i+dst][j | (1 << inxt)][inxt], nval)

maxval = max(max(dp[30][j][k] for k in range(len(relevant))) for j in range(1 << len(relevant)))
print(maxval)


