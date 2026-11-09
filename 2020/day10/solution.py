import sys
from collections import Counter

adapters = sorted(map(int, sys.stdin.read().split()))
chain = [0] + adapters + [adapters[-1] + 3]
gaps = Counter(b - a for a, b in zip(chain, chain[1:]))
print(gaps[1] * gaps[3])
