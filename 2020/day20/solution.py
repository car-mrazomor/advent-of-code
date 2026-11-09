import re
import sys
from collections import Counter
from math import prod

tiles = {}
for block in sys.stdin.read().strip().split("\n\n"):
    head, *rows = block.splitlines()
    tiles[int(re.search(r"\d+", head)[0])] = rows


def edges(rows):
    sides = [rows[0], rows[-1], "".join(r[0] for r in rows), "".join(r[-1] for r in rows)]
    return [min(s, s[::-1]) for s in sides]


count = Counter(edge for rows in tiles.values() for edge in edges(rows))
print(prod(tile for tile, rows in tiles.items() if sum(count[e] == 1 for e in edges(rows)) == 2))
