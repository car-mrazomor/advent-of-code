import sys

grid = sys.stdin.read().split()
rows, cols = len(grid), len(grid[0])
seen = set()
total = 0
for y in range(rows):
    for x in range(cols):
        if (y, x) in seen:
            continue
        plant, area, perimeter = grid[y][x], 0, 0
        stack = [(y, x)]
        seen.add((y, x))
        while stack:
            cy, cx = stack.pop()
            area += 1
            for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == plant:
                    if (ny, nx) not in seen:
                        seen.add((ny, nx))
                        stack.append((ny, nx))
                else:
                    perimeter += 1
        total += area * perimeter
print(total)
