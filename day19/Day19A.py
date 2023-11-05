from collections import deque
from math import ceil

lines = [l.strip() for l in open("../input.txt").readlines()]

# (time, ore robots, ore, clay robots, clay, obsidian robots, obsidian, geode robots, geodes)
# indices 6, 12, (18, 21), (27, 30)

finalans = 0


for idx, ls in enumerate(lines):
    line = ls.split()
    cost_ore = int(line[6])
    cost_clay = int(line[12])
    cost_obs_ore = int(line[18])
    cost_obs_clay = int(line[21])
    cost_geo_ore = int(line[27])
    cost_geo_obs = int(line[30])
    max_ore = max(cost_ore, cost_clay, cost_obs_ore, cost_geo_ore)
    max_clay = cost_obs_clay
    max_obs = cost_geo_obs
    ans = 0
    q = deque()
    q.append((0, 1, 0, 0, 0, 0, 0, 0, 0))
    seen = set()
    maxtime = 24
    while q:
        time, ore_bots, ore, clay_bots, clay, obs_bots, obs, geo_bots, geo = q.popleft()
        if time > maxtime:
            continue

        if (time, ore_bots, ore, clay_bots, clay, obs_bots, obs, geo_bots, geo) in seen:
            continue
        seen.add((time, ore_bots, ore, clay_bots, clay, obs_bots, obs, geo_bots, geo))

        # when is the next time we want to create any type of bot?

        # ore bot
        if ore_bots < max_ore:
            ntime = ceil((cost_ore-ore)/ore_bots)+1
            if ntime < 1:
                ntime = 1
            ore_cnt = ore+(ore_bots*ntime) - cost_ore
            clay_cnt = clay+(clay_bots*ntime)
            obs_cnt = obs+(obs_bots*ntime)
            geo_cnt = geo+(geo_bots*ntime)
            q.append((time+ntime, ore_bots+1, ore_cnt, clay_bots, clay_cnt, obs_bots, obs_cnt, geo_bots, geo_cnt))

        # clay bot

        if clay_bots < max_clay:
            ntime = ceil((cost_clay-ore)/ore_bots)+1
            if ntime < 1:
                ntime = 1

            ore_cnt = ore + (ore_bots * ntime) - cost_clay
            clay_cnt = clay + (clay_bots * ntime)
            obs_cnt = obs + (obs_bots * ntime)
            geo_cnt = geo + (geo_bots * ntime)
            q.append((time + ntime, ore_bots, ore_cnt, clay_bots+1, clay_cnt, obs_bots, obs_cnt, geo_bots, geo_cnt))

        # obsidian bot

        if obs_bots < max_obs:
            if clay_bots > 0:
                ntime = max(ceil((cost_obs_ore-ore)/ore_bots), ceil((cost_obs_clay-clay)/clay_bots))+1
                if ntime < 1:
                    ntime = 1

                ore_cnt = ore + (ore_bots * ntime) - cost_obs_ore
                clay_cnt = clay + (clay_bots * ntime) - cost_obs_clay
                obs_cnt = obs + (obs_bots * ntime)
                geo_cnt = geo + (geo_bots * ntime)
                q.append((time + ntime, ore_bots, ore_cnt, clay_bots, clay_cnt, obs_bots+1, obs_cnt, geo_bots, geo_cnt))

        # geode bot

        if obs_bots > 0:
            ntime = max(ceil((cost_geo_ore - ore) / ore_bots), ceil((cost_geo_obs - obs) / obs_bots))+1
            if ntime < 1:
                ntime = 1

            ore_cnt = ore + (ore_bots * ntime) - cost_geo_ore
            clay_cnt = clay + (clay_bots * ntime)
            obs_cnt = obs + (obs_bots * ntime) - cost_geo_obs
            geo_cnt = geo + (geo_bots * ntime)
            q.append((time + ntime, ore_bots, ore_cnt, clay_bots, clay_cnt, obs_bots, obs_cnt, geo_bots+1, geo_cnt))

        # or we could just stop right here
        ans = max(ans, (maxtime - time)*geo_bots + geo)

    print(ans)
    finalans+=((idx+1)*ans)
    print(f"Blueprint {(idx+1)} done")
print(finalans)