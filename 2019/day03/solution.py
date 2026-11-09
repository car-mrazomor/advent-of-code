import sys

STEP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def visited(path):
    x = y = 0
    seen = set()
    for move in path.split(","):
        dx, dy = STEP[move[0]]
        for _ in range(int(move[1:])):
            x, y = x + dx, y + dy
            seen.add((x, y))
    return seen


first, second = sys.stdin.read().split()
print(min(abs(x) + abs(y) for x, y in visited(first) & visited(second)))
