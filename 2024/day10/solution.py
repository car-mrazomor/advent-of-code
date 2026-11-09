import sys

grid = [list(map(int, row)) for row in sys.stdin.read().split()]
rows, cols = len(grid), len(grid[0])


def peaks(y, x):
    if grid[y][x] == 9:
        return {(y, x)}
    found = set()
    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == grid[y][x] + 1:
            found |= peaks(ny, nx)
    return found


print(sum(len(peaks(y, x)) for y in range(rows) for x in range(cols) if grid[y][x] == 0))
