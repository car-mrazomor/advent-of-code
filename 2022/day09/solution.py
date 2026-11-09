import sys

STEP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
hx = hy = tx = ty = 0
visited = {(0, 0)}
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    direction, count = line.split()
    dx, dy = STEP[direction]
    for _ in range(int(count)):
        hx, hy = hx + dx, hy + dy
        if abs(hx - tx) > 1 or abs(hy - ty) > 1:
            tx += (hx > tx) - (hx < tx)
            ty += (hy > ty) - (hy < ty)
            visited.add((tx, ty))
print(len(visited))
