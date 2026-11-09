import sys
from math import prod

lines = sys.stdin.read().rstrip("\n").split("\n")
width = max(map(len, lines))
rows = [line.ljust(width) for line in lines]
digits, ops = rows[:-1], rows[-1]

blank = [all(row[c] == " " for row in rows) for c in range(width)]
problems, start = [], 0
for c in range(width + 1):
    if c == width or blank[c]:
        if c > start:
            problems.append((start, c))
        start = c + 1


def solve(read_columns):
    total = 0
    for a, b in problems:
        op = ops[a:b].strip()
        if read_columns:
            numbers = [int("".join(r[c] for r in digits).strip()) for c in range(b - 1, a - 1, -1)
                       if "".join(r[c] for r in digits).strip()]
        else:
            numbers = [int(r[a:b]) for r in digits if r[a:b].strip()]
        total += sum(numbers) if op == "+" else prod(numbers)
    return total


print(solve(False))
print(solve(True))
