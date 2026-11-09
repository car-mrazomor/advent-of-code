import json
import sys
from functools import reduce


def flatten(tree, depth=0):
    if isinstance(tree, int):
        return [[tree, depth]]
    return flatten(tree[0], depth + 1) + flatten(tree[1], depth + 1)


def reduce_number(flat):
    while True:
        for i, (value, depth) in enumerate(flat):
            if depth > 4:
                left, right = flat[i][0], flat[i + 1][0]
                if i > 0:
                    flat[i - 1][0] += left
                if i + 2 < len(flat):
                    flat[i + 2][0] += right
                flat[i:i + 2] = [[0, depth - 1]]
                break
        else:
            for i, (value, depth) in enumerate(flat):
                if value >= 10:
                    flat[i:i + 1] = [[value // 2, depth + 1], [value - value // 2, depth + 1]]
                    break
            else:
                return flat


def add(a, b):
    return reduce_number([[v, d + 1] for v, d in a + b])


def magnitude(flat):
    flat = [list(x) for x in flat]
    while len(flat) > 1:
        deepest = max(d for _, d in flat)
        i = next(i for i, (_, d) in enumerate(flat) if d == deepest)
        flat[i:i + 2] = [[3 * flat[i][0] + 2 * flat[i + 1][0], deepest - 1]]
    return flat[0][0]


numbers = [flatten(json.loads(line)) for line in sys.stdin.read().split()]
print(magnitude(reduce(add, numbers)))
