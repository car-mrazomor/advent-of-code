import copy
import sys
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

MOVES = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

start = Intcode.load(sys.stdin.read())
queue = deque([((0, 0), start, 0)])
seen = {(0, 0)}
while queue:
    (x, y), droid, steps = queue.popleft()
    for command, (dx, dy) in MOVES.items():
        spot = (x + dx, y + dy)
        if spot in seen:
            continue
        seen.add(spot)
        moved = copy.deepcopy(droid)
        status = moved.run(command)[0]
        if status == 2:
            print(steps + 1)
            sys.exit()
        if status == 1:
            queue.append((spot, moved, steps + 1))
