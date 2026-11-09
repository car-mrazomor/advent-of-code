import sys
from math import gcd

grid = sys.stdin.read().split()
asteroids = [(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "#"]


def visible(station):
    sx, sy = station
    directions = set()
    for x, y in asteroids:
        if (x, y) != station:
            dx, dy = x - sx, y - sy
            g = gcd(dx, dy)
            directions.add((dx // g, dy // g))
    return len(directions)


print(max(visible(a) for a in asteroids))
