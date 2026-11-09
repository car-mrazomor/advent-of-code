import sys

grid = sys.stdin.read().split()
LINKS = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
STEP = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
OPPOSITE = {"N": "S", "S": "N", "E": "W", "W": "E"}

sy = next(y for y, row in enumerate(grid) if "S" in row)
sx = grid[sy].index("S")


def tile(x, y):
    return grid[y][x] if 0 <= y < len(grid) and 0 <= x < len(grid[y]) else "."


heading = next(d for d, (dx, dy) in STEP.items() if OPPOSITE[d] in LINKS.get(tile(sx + dx, sy + dy), ""))
x, y, length = sx, sy, 0
while True:
    dx, dy = STEP[heading]
    x, y, length = x + dx, y + dy, length + 1
    if (x, y) == (sx, sy):
        break
    heading = LINKS[tile(x, y)].replace(OPPOSITE[heading], "", 1)
print(length // 2)
