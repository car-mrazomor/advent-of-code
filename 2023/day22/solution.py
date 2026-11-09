import sys

bricks = sorted((tuple(map(int, a.split(","))), tuple(map(int, b.split(","))))
                for a, b in (line.split("~") for line in sys.stdin.read().split()))
bricks.sort(key=lambda b: b[0][2])
top = {}
supports, supported_by = {}, {}
for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
    cells = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
    floor = max((top[c][0] for c in cells if c in top), default=0)
    below = {top[c][1] for c in cells if c in top and top[c][0] == floor}
    supported_by[i] = below
    supports[i] = set()
    for j in below:
        supports[j].add(i)
    height = floor + 1 + (z2 - z1)
    for c in cells:
        top[c] = (height, i)
print(sum(all(len(supported_by[k]) > 1 for k in supports[i]) for i in range(len(bricks))))
