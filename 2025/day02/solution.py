import re
import sys

ranges = [(int(a), int(b)) for a, b in re.findall(r"(\d+)-(\d+)", sys.stdin.read())]
digits = len(str(max(b for _, b in ranges)))


def repeated(exactly_twice):
    found = set()
    for length in range(2, digits + 1):
        for size in range(1, length // 2 + 1):
            times = length // size
            if length % size or (exactly_twice and times != 2):
                continue
            for base in range(10 ** (size - 1), 10 ** size):
                found.add(int(str(base) * times))
    return found


for twice in (True, False):
    print(sum(n for n in repeated(twice) if any(a <= n <= b for a, b in ranges)))
