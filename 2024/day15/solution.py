import sys

warehouse, moves = sys.stdin.read().split("\n\n")
grid = [list(row) for row in warehouse.split()]
y = next(i for i, row in enumerate(grid) if "@" in row)
x = grid[y].index("@")
STEP = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
for move in moves.replace("\n", ""):
    dy, dx = STEP[move]
    ey, ex = y + dy, x + dx
    while grid[ey][ex] == "O":
        ey, ex = ey + dy, ex + dx
    if grid[ey][ex] == "#":
        continue
    grid[ey][ex] = "O"
    grid[y][x] = "."
    y, x = y + dy, x + dx
    grid[y][x] = "@"
print(sum(100 * r + c for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == "O"))
