import re
import sys
from functools import cache

rules = {}
for line in sys.stdin.read().splitlines():
    outer, inner = line.split(" bags contain ")
    rules[outer] = {name: int(n) for n, name in re.findall(r"(\d+) (\w+ \w+) bag", inner)}


@cache
def holds_gold(bag):
    return any(inner == "shiny gold" or holds_gold(inner) for inner in rules[bag])


@cache
def inside(bag):
    return sum(n * (1 + inside(inner)) for inner, n in rules[bag].items())


print(sum(holds_gold(bag) for bag in rules))
print(inside("shiny gold"))
