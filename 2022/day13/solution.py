import json
import sys


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a > b) - (a < b)
    a = a if isinstance(a, list) else [a]
    b = b if isinstance(b, list) else [b]
    for x, y in zip(a, b):
        if result := compare(x, y):
            return result
    return (len(a) > len(b)) - (len(a) < len(b))


pairs = [list(map(json.loads, block.split())) for block in sys.stdin.read().strip().split("\n\n")]
print(sum(i for i, (a, b) in enumerate(pairs, 1) if compare(a, b) < 0))
