import re
import sys

rules, _, nearby = sys.stdin.read().split("\n\n")
ranges = [(int(a), int(b)) for a, b in re.findall(r"(\d+)-(\d+)", rules)]
values = [int(v) for v in re.findall(r"\d+", nearby.split(":", 1)[1])]
print(sum(v for v in values if not any(a <= v <= b for a, b in ranges)))
