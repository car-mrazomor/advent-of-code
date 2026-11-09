import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

robot = Intcode.load(sys.stdin.read())
panels = {}
x = y = 0
dx, dy = 0, -1
while not robot.halted:
    out = robot.run(panels.get((x, y), 0))
    if len(out) < 2:
        break
    panels[(x, y)] = out[0]
    dx, dy = (-dy, dx) if out[1] else (dy, -dx)
    x, y = x + dx, y + dy
print(len(panels))
