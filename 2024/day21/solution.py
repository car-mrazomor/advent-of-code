import sys
from functools import cache

NUMERIC = {c: (r, k) for r, row in enumerate(["789", "456", "123", " 0A"]) for k, c in enumerate(row)}
ARROWS = {c: (r, k) for r, row in enumerate([" ^A", "<v>"]) for k, c in enumerate(row)}


def routes(pad, a, b):
    (r1, c1), (r2, c2) = pad[a], pad[b]
    vertical = ("v" if r2 > r1 else "^") * abs(r2 - r1)
    horizontal = (">" if c2 > c1 else "<") * abs(c2 - c1)
    gap = pad[" "]
    options = set()
    if (r1, c2) != gap:
        options.add(horizontal + vertical + "A")
    if (r2, c1) != gap:
        options.add(vertical + horizontal + "A")
    return options


@cache
def presses(sequence, robots, numeric=False):
    if robots == 0:
        return len(sequence)
    pad = NUMERIC if numeric else ARROWS
    total, at = 0, "A"
    for key in sequence:
        total += min(presses(route, robots - 1) for route in routes(pad, at, key))
        at = key
    return total


print(sum(presses(code, 3, True) * int(code[:-1]) for code in sys.stdin.read().split()))
