import sys
from collections import deque

kinds, targets, flips, memory = {}, {}, {}, {}
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    name, outs = line.split(" -> ")
    kind = name[0] if name[0] in "%&" else ""
    name = name.lstrip("%&")
    kinds[name], targets[name] = kind, outs.split(", ")
for name, outs in targets.items():
    for out in outs:
        memory.setdefault(out, {})[name] = False
flips = {name: False for name, kind in kinds.items() if kind == "%"}

counts = [0, 0]
for _ in range(1000):
    queue = deque([("button", "broadcaster", False)])
    while queue:
        source, name, high = queue.popleft()
        counts[high] += 1
        kind = kinds.get(name)
        if kind == "%":
            if high:
                continue
            flips[name] = not flips[name]
            send = flips[name]
        elif kind == "&":
            memory[name][source] = high
            send = not all(memory[name].values())
        elif name == "broadcaster":
            send = high
        else:
            continue
        for out in targets[name]:
            queue.append((name, out, send))
print(counts[0] * counts[1])
