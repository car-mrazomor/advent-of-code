import sys

score = 0
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    them, me = "ABC".index(line[0]), "XYZ".index(line[2])
    score += me + 1 + 3 * ((me - them + 1) % 3)
print(score)
