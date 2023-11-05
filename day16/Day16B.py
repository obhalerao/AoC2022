lines = [l.strip() for l in open("../input.txt").readlines()]

rates = {}

edges = {}

for line in lines:
    ls = line.split()
    cur_valve = ls[1]
    edges[cur_valve] = []
    rate = int(ls[4].split('=')[-1][:-1])
    rates[cur_valve] = rate
    for nxt in ls[9:]:
        nnxt = nxt
        if nxt[-1] == ',':
            nnxt = nxt[:-1]
        edges[cur_valve].append(nnxt)

relevant = []
total = []
for idx in rates:
    if rates[idx] > 0:
        total.append(idx)
        relevant.append(idx)

relset = set(relevant)
for idx in rates:
    if idx not in relset:
        total.append(idx)

invrelevant = {i:idx for idx, i in enumerate(relevant)}
invtotal = {i:idx for idx,i in enumerate(total)}

nedges = {}
for i in edges:
    nedges[invtotal[i]] = []
    for j in edges[i]:
        nedges[invtotal[i]].append(invtotal[j])

print(len(total)*len(total)*(1<<len(relevant))*2)

dp = [[[[float("-inf") for k in range(len(total))] for l in range(len(total))] for j in range(1 << len(relevant))] for i in range(2)]

dp[0][0][invtotal['AA']][invtotal['AA']] = 0

for i in range(26):
    print(i)
    for j in range(1 << len(relevant)):
        if j % 1000 == 0:
            print(j)
        tot = 0
        for k in range(len(relevant)):
            if j & (1 << k) > 0:
                tot+=rates[relevant[k]]
        for k in range(len(total)):
            for l in range(len(total)):
                # transition 1: open both k and l
                if k < len(relevant) and l < len(relevant) and (j & (1 << k)) == 0 and (j & (1 << l)) == 0:
                    nj = j | ((1 << k) | (1 << l))
                    dp[1][nj][k][l] = max(dp[1][nj][k][l], dp[0][j][k][l]+tot)
                # transition 2: open k, traverse l
                if k < len(relevant) and (j & (1 << k)) == 0:
                    nj = j | (1 << k)
                    for idx in nedges[l]:
                        dp[1][nj][k][idx] = max(dp[1][nj][k][idx], dp[0][j][k][l]+tot)
                # transition 3: traverse k, open l
                if l < len(relevant) and (j & (1 << l)) == 0:
                    nj = j | (1 << l)
                    for idx in nedges[k]:
                        dp[1][nj][idx][l] = max(dp[1][nj][idx][l], dp[0][j][k][l]+tot)
                # transition 4: traverse both k and l
                for idx1 in nedges[k]:
                    for idx2 in nedges[l]:
                        dp[1][j][idx1][idx2] = max(dp[1][j][idx1][idx2], dp[0][j][k][l]+tot)
    # sub out the dp array
    print(f"done with {i}")
    dp[0] = dp[1]
    dp[1] = [[[float("-inf") for l in range(len(total))] for k in range(len(total))] for j in range(1 << len(relevant))]

print(max(max(max(i) for i in j) for j in dp[0]))