import re
import sys

board, path = sys.stdin.read().rstrip("\n").split("\n\n")
rows = board.split("\n")
width = max(map(len, rows))
grid = [row.ljust(width) for row in rows]
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

y, x, facing = 0, grid[0].index("."), 0
for step in re.findall(r"\d+|[LR]", path):
    if step == "R":
        facing = (facing + 1) % 4
        continue
    if step == "L":
        facing = (facing - 1) % 4
        continue
    dy, dx = MOVES[facing]
    for _ in range(int(step)):
        ny, nx = (y + dy) % len(grid), (x + dx) % width
        while grid[ny][nx] == " ":
            ny, nx = (ny + dy) % len(grid), (nx + dx) % width
        if grid[ny][nx] == "#":
            break
        y, x = ny, nx
print(1000 * (y + 1) + 4 * (x + 1) + facing)
