import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

view = "".join(map(chr, Intcode.load(sys.stdin.read()).run())).split()
total = 0
for y in range(1, len(view) - 1):
    for x in range(1, len(view[y]) - 1):
        if all(view[y + dy][x + dx] == "#" for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))):
            total += x * y
print(total)
