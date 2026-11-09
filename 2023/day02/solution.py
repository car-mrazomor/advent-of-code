import re
import sys

LIMIT = {"red": 12, "green": 13, "blue": 14}
possible = power = 0
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    game = int(re.match(r"Game (\d+)", line)[1])
    most = {"red": 0, "green": 0, "blue": 0}
    for count, color in re.findall(r"(\d+) (red|green|blue)", line):
        most[color] = max(most[color], int(count))
    if all(most[c] <= LIMIT[c] for c in LIMIT):
        possible += game
    power += most["red"] * most["green"] * most["blue"]
print(possible)
print(power)
