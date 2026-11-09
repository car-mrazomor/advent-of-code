import sys
from functools import cache


def arrangements(springs, groups):
    @cache
    def count(i, g):
        if g == len(groups):
            return "#" not in springs[i:]
        if i >= len(springs):
            return 0
        total = 0
        if springs[i] in ".?":
            total += count(i + 1, g)
        size = groups[g]
        if (springs[i] in "#?" and i + size <= len(springs) and "." not in springs[i:i + size]
                and (i + size == len(springs) or springs[i + size] != "#")):
            total += count(i + size + 1, g + 1)
        return total

    return count(0, 0)


total = 0
for line in sys.stdin.read().splitlines():
    if line.strip():
        springs, groups = line.split()
        total += arrangements(springs, tuple(map(int, groups.split(","))))
print(total)
