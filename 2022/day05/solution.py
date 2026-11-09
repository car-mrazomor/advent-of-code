import re
import sys

drawing, moves = sys.stdin.read().split("\n\n")
rows = drawing.splitlines()
count = len(rows[-1].split())
stacks = [[] for _ in range(count)]
for row in reversed(rows[:-1]):
    for i in range(count):
        if 1 + 4 * i < len(row) and row[1 + 4 * i].isalpha():
            stacks[i].append(row[1 + 4 * i])
for n, src, dst in re.findall(r"move (\d+) from (\d+) to (\d+)", moves):
    for _ in range(int(n)):
        stacks[int(dst) - 1].append(stacks[int(src) - 1].pop())
print("".join(s[-1] for s in stacks if s))
