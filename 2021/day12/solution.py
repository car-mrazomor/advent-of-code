import sys
from collections import defaultdict

links = defaultdict(set)
for line in sys.stdin.read().split():
    a, b = line.split("-")
    links[a].add(b)
    links[b].add(a)


def paths(cave, seen):
    if cave == "end":
        return 1
    return sum(paths(n, seen | {n}) for n in links[cave] if n.isupper() or n not in seen)


print(paths("start", {"start"}))
