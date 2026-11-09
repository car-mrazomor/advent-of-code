import heapq
import sys
from collections import deque

grid = sys.stdin.read().split()
points = {c: (x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "@" or c.islower()}
all_keys = sum(1 << (ord(c) - 97) for c in points if c.islower())


def reachable(start):
    found, seen = {}, {start}
    queue = deque([(start, 0, 0)])
    while queue:
        (x, y), steps, doors = queue.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            c = grid[ny][nx]
            if c == "#" or (nx, ny) in seen:
                continue
            seen.add((nx, ny))
            need = doors | (1 << (ord(c) - 65)) if c.isupper() else doors
            if c.islower():
                found[c] = (steps + 1, need)
            queue.append(((nx, ny), steps + 1, need))
    return found


edges = {name: reachable(pos) for name, pos in points.items()}
best = {("@", 0): 0}
heap = [(0, "@", 0)]
while heap:
    steps, at, keys = heapq.heappop(heap)
    if keys == all_keys:
        print(steps)
        break
    if steps > best.get((at, keys), 1 << 60):
        continue
    for key, (dist, need) in edges[at].items():
        bit = 1 << (ord(key) - 97)
        if keys & bit or need & ~keys:
            continue
        state = (key, keys | bit)
        if steps + dist < best.get(state, 1 << 60):
            best[state] = steps + dist
            heapq.heappush(heap, (steps + dist, key, keys | bit))
