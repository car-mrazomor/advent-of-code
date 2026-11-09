import sys
from collections import defaultdict
from itertools import permutations

grid = sys.stdin.read().split()
antennas = defaultdict(list)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c != ".":
            antennas[c].append((x, y))
spots = {(2 * x2 - x1, 2 * y2 - y1) for points in antennas.values() for (x1, y1), (x2, y2) in permutations(points, 2)}
print(sum(0 <= x < len(grid[0]) and 0 <= y < len(grid) for x, y in spots))
