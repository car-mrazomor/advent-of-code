import re
import sys


def geodes(ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs, minutes):
    max_ore = max(ore_ore, clay_ore, obs_ore, geo_ore)
    best = 0

    def search(time, robots, stock, made):
        nonlocal best
        r_ore, r_clay, r_obs = robots
        ore, clay, obs = stock
        best = max(best, made)
        if time <= 1 or made + time * (time - 1) // 2 <= best:
            return
        options = []
        if r_obs:
            options.append((geo_ore, 0, geo_obs, 3))
        if r_clay and r_obs < geo_obs:
            options.append((obs_ore, obs_clay, 0, 2))
        if r_clay < obs_clay:
            options.append((clay_ore, 0, 0, 1))
        if r_ore < max_ore:
            options.append((ore_ore, 0, 0, 0))
        for need_ore, need_clay, need_obs, kind in options:
            wait = 0
            while (ore + r_ore * wait < need_ore or clay + r_clay * wait < need_clay
                   or obs + r_obs * wait < need_obs):
                wait += 1
            left = time - wait - 1
            if left <= 0:
                continue
            new_stock = (ore + r_ore * (wait + 1) - need_ore, clay + r_clay * (wait + 1) - need_clay,
                         obs + r_obs * (wait + 1) - need_obs)
            if kind == 3:
                search(left, robots, new_stock, made + left)
            else:
                new_robots = list(robots)
                new_robots[kind] += 1
                search(left, tuple(new_robots), new_stock, made)

    search(minutes, (1, 0, 0), (0, 0, 0), 0)
    return best


total = 0
for chunk in sys.stdin.read().split("Blueprint")[1:]:
    number, *costs = map(int, re.findall(r"\d+", chunk))
    total += number * geodes(*costs, 24)
print(total)
