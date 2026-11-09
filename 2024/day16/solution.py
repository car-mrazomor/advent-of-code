import heapq
import sys

grid = sys.stdin.read().split()
start = next((y, x) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "S")
best = {(start, (0, 1)): 0}
heap = [(0, start, (0, 1))]
while heap:
    score, (y, x), (dy, dx) = heapq.heappop(heap)
    if grid[y][x] == "E":
        print(score)
        break
    if score > best.get(((y, x), (dy, dx)), 1 << 60):
        continue
    for cost, pos, facing in ((score + 1, (y + dy, x + dx), (dy, dx)),
                              (score + 1000, (y, x), (dx, -dy)),
                              (score + 1000, (y, x), (-dx, dy))):
        if grid[pos[0]][pos[1]] != "#" and cost < best.get((pos, facing), 1 << 60):
            best[(pos, facing)] = cost
            heapq.heappush(heap, (cost, pos, facing))
