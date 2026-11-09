import sys

seeds_text, *sections = sys.stdin.read().strip().split("\n\n")
values = list(map(int, seeds_text.split(":")[1].split()))
for section in sections:
    ranges = [tuple(map(int, line.split())) for line in section.splitlines()[1:]]
    values = [next((dst + v - src for dst, src, n in ranges if src <= v < src + n), v) for v in values]
print(min(values))
