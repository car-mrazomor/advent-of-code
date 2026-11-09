import sys
from math import prod

grid = sys.stdin.read().split()


def trees(right, down):
    return sum(row[(i * right) % len(row)] == "#" for i, row in enumerate(grid[::down]))


print(trees(3, 1))
print(prod(trees(r, d) for r, d in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
