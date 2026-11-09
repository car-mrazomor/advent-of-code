import sys
from collections import defaultdict

sizes = defaultdict(int)
path = []
for line in sys.stdin.read().splitlines():
    parts = line.split()
    if parts[:2] == ["$", "cd"]:
        if parts[2] == "/":
            path = []
        elif parts[2] == "..":
            path.pop()
        else:
            path.append(parts[2])
    elif parts and parts[0].isdigit():
        for i in range(len(path) + 1):
            sizes[tuple(path[:i])] += int(parts[0])
print(sum(size for size in sizes.values() if size <= 100000))
