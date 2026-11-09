import sys
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

program = sys.stdin.read()


def signal(phases):
    value = 0
    for phase in phases:
        value = Intcode.load(program).run(phase, value)[-1]
    return value


print(max(signal(p) for p in permutations(range(5))))
