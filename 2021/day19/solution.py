import sys
from collections import Counter
from itertools import permutations, product

scanners = [{tuple(map(int, line.split(","))) for line in block.splitlines()[1:]}
            for block in sys.stdin.read().strip().split("\n\n")]


def det(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


ROTATIONS = []
for perm in permutations(range(3)):
    for signs in product((1, -1), repeat=3):
        m = [[signs[r] if c == perm[r] else 0 for c in range(3)] for r in range(3)]
        if det(m) == 1:
            ROTATIONS.append(m)


def rotate(points, m):
    return {tuple(sum(m[r][c] * p[c] for c in range(3)) for r in range(3)) for p in points}


known = set(scanners[0])
pending = scanners[1:]
while pending:
    for scanner in list(pending):
        for m in ROTATIONS:
            turned = rotate(scanner, m)
            shifts = Counter(tuple(a[i] - b[i] for i in range(3)) for a in known for b in turned)
            shift, hits = shifts.most_common(1)[0]
            if hits >= 12:
                known |= {tuple(p[i] + shift[i] for i in range(3)) for p in turned}
                pending.remove(scanner)
                break
print(len(known))
