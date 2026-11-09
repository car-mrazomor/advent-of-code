import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

out = Intcode.load(sys.stdin.read()).run()
print(sum(1 for tile in out[2::3] if tile == 2))
