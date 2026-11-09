import re
import sys
from functools import cache

rates, links = {}, {}
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    name, rate, *others = re.findall(r"[A-Z]{2}|\d+", line[1:])
    rates[name], links[name] = int(rate), others

dist = {a: {b: 0 if a == b else (1 if b in links[a] else 99) for b in rates} for a in rates}
for k in rates:
    for i in rates:
        for j in rates:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
useful = [v for v in rates if rates[v]]
bit = {v: 1 << i for i, v in enumerate(useful)}


@cache
def best(at, time, opened):
    result = 0
    for v in useful:
        left = time - dist[at][v] - 1
        if left > 0 and not opened & bit[v]:
            result = max(result, rates[v] * left + best(v, left, opened | bit[v]))
    return result


print(best("AA", 30, 0))
