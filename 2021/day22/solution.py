import re
import sys
from collections import Counter

cuboids = Counter()
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    on = line.startswith("on")
    x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", line))
    box = (max(x1, -50), min(x2, 50), max(y1, -50), min(y2, 50), max(z1, -50), min(z2, 50))
    if box[0] > box[1] or box[2] > box[3] or box[4] > box[5]:
        continue
    update = Counter()
    for (a1, a2, b1, b2, c1, c2), sign in cuboids.items():
        overlap = (max(a1, box[0]), min(a2, box[1]), max(b1, box[2]), min(b2, box[3]), max(c1, box[4]), min(c2, box[5]))
        if overlap[0] <= overlap[1] and overlap[2] <= overlap[3] and overlap[4] <= overlap[5]:
            update[overlap] -= sign
    if on:
        update[box] += 1
    cuboids.update(update)
print(sum((x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * sign for (x1, x2, y1, y2, z1, z2), sign in cuboids.items()))
