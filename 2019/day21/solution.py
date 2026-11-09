import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

SCRIPT = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""
out = Intcode.load(sys.stdin.read()).run(*map(ord, SCRIPT))
print(out[-1] if out[-1] > 127 else "".join(map(chr, out)))
