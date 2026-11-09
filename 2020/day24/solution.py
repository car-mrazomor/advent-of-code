import re
import sys

STEPS = {"e": (1, 0), "w": (-1, 0), "ne": (1, -1), "nw": (0, -1), "se": (0, 1), "sw": (-1, 1)}

black = set()
for line in sys.stdin.read().split():
    q = r = 0
    for step in re.findall(r"e|w|ne|nw|se|sw", line):
        dq, dr = STEPS[step]
        q, r = q + dq, r + dr
    black ^= {(q, r)}
print(len(black))
