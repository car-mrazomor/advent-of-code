import re
import sys


def evaluate(tokens):
    value, op = 0, "+"
    while tokens:
        token = tokens.pop(0)
        if token == ")":
            break
        if token in "+*":
            op = token
            continue
        number = evaluate(tokens) if token == "(" else int(token)
        value = value + number if op == "+" else value * number
    return value


print(sum(evaluate(re.findall(r"\d+|[()+*]", line)) for line in sys.stdin.read().splitlines() if line.strip()))
