import re
import sys
from functools import cache

*shape_blocks, region_block = sys.stdin.read().strip().split("\n\n")
shapes = []
for block in shape_blocks:
    rows = block.splitlines()[1:]
    shapes.append({(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == "#"})


def orientations(cells):
    found = set()
    for _ in range(4):
        cells = {(c, -r) for r, c in cells}
        for variant in (cells, {(r, -c) for r, c in cells}):
            top = min(variant)
            found.add(tuple(sorted((r - top[0], c - top[1]) for r, c in variant)))
    return list(found)


ORIENTED = [orientations(s) for s in shapes]


def fits(width, height, counts):
    needed = sum(n * len(shapes[i]) for i, n in enumerate(counts))
    if needed > width * height:
        return False
    if (width // 3) * (height // 3) >= sum(counts):
        return True

    @cache
    def search(filled, remaining, slack):
        if not any(remaining):
            return True
        spot = next(p for p in range(width * height) if not filled >> p & 1)
        r0, c0 = divmod(spot, width)
        for i, left in enumerate(remaining):
            if not left:
                continue
            for shape in ORIENTED[i]:
                mask = 0
                for dr, dc in shape:
                    r, c = r0 + dr, c0 + dc
                    if not (0 <= r < height and 0 <= c < width) or filled >> (r * width + c) & 1:
                        break
                    mask |= 1 << (r * width + c)
                else:
                    rest = remaining[:i] + (left - 1,) + remaining[i + 1:]
                    if search(filled | mask, rest, slack):
                        return True
        return slack > 0 and search(filled | 1 << spot, remaining, slack - 1)

    return search(0, tuple(counts), width * height - needed)


total = 0
for line in region_block.splitlines():
    width, height, *counts = map(int, re.findall(r"\d+", line))
    total += fits(width, height, counts)
print(total)
