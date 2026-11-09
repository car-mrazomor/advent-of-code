import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

program = sys.stdin.read()
nodes = [Intcode.load(program, [address]) for address in range(50)]
queues = [[] for _ in nodes]
while True:
    for address, node in enumerate(nodes):
        out = node.run(*(queues[address] or [-1]))
        queues[address] = []
        for i in range(0, len(out), 3):
            to, x, y = out[i:i + 3]
            if to == 255:
                print(y)
                sys.exit()
            queues[to] += [x, y]
