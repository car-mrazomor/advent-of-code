import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

program = sys.stdin.read()
print(sum(Intcode.load(program).run(x, y)[0] for x in range(50) for y in range(50)))
