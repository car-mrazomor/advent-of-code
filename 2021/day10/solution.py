import sys

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def first_illegal(line):
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(PAIRS[c])
        elif not stack or stack.pop() != c:
            return c
    return None


print(sum(POINTS.get(first_illegal(line), 0) for line in sys.stdin.read().split()))
