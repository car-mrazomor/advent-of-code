import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

print(Intcode.load(sys.stdin.read()).run(1)[-1])
