import sys

range_text, ids = sys.stdin.read().strip().split("\n\n")
ranges = sorted(tuple(map(int, line.split("-"))) for line in range_text.split())
print(sum(any(a <= int(i) <= b for a, b in ranges) for i in ids.split()))

total, end = 0, -1
for a, b in ranges:
    start = max(a, end + 1)
    if b >= start:
        total += b - start + 1
        end = b
print(total)
