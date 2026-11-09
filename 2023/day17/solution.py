import heapq
import sys

grid = [list(map(int, row)) for row in sys.stdin.read().split()]
rows, cols = len(grid), len(grid[0])
heap = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]
best = {}
while heap:
    heat, y, x, dy, dx, run = heapq.heappop(heap)
    if (y, x) == (rows - 1, cols - 1):
        print(heat)
        break
    if best.get((y, x, dy, dx, run), 1 << 60) < heat:
        continue
    for ndy, ndx in ((dy, dx), (dx, dy), (-dx, -dy)):
        nrun = run + 1 if (ndy, ndx) == (dy, dx) else 1
        ny, nx = y + ndy, x + ndx
        if nrun > 3 or not (0 <= ny < rows and 0 <= nx < cols):
            continue
        state = (ny, nx, ndy, ndx, nrun)
        cost = heat + grid[ny][nx]
        if cost < best.get(state, 1 << 60):
            best[state] = cost
            heapq.heappush(heap, (cost, ny, nx, ndy, ndx, nrun))
