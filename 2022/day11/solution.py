import re
import sys
from math import prod

monkeys = []
for block in sys.stdin.read().strip().split("\n\n"):
    lines = block.splitlines()
    monkeys.append({
        "items": list(map(int, re.findall(r"\d+", lines[1]))),
        "op": lines[2].split("= ")[1],
        "test": int(lines[3].split()[-1]),
        "yes": int(lines[4].split()[-1]),
        "no": int(lines[5].split()[-1]),
        "seen": 0,
    })
for _ in range(20):
    for m in monkeys:
        for old in m["items"]:
            new = eval(m["op"], {"old": old}) // 3
            monkeys[m["yes"] if new % m["test"] == 0 else m["no"]]["items"].append(new)
        m["seen"] += len(m["items"])
        m["items"] = []
print(prod(sorted(m["seen"] for m in monkeys)[-2:]))
