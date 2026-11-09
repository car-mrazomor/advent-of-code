import sys
from collections import defaultdict

links = defaultdict(set)
for line in sys.stdin.read().split():
    a, b = line.split("-")
    links[a].add(b)
    links[b].add(a)
triangles = {frozenset((a, b, c)) for a in links for b in links[a] for c in links[a] & links[b]}
print(sum(any(name.startswith("t") for name in t) for t in triangles))
