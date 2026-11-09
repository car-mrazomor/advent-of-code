import sys
from collections import Counter

ORDER = "23456789TJQKA"


def strength(hand):
    shape = sorted(Counter(hand).values(), reverse=True)
    return shape, [ORDER.index(c) for c in hand]


hands = [line.split() for line in sys.stdin.read().splitlines() if line.strip()]
hands.sort(key=lambda h: strength(h[0]))
print(sum(rank * int(bid) for rank, (_, bid) in enumerate(hands, 1)))
