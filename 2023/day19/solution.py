import re
import sys

flow_text, part_text = sys.stdin.read().strip().split("\n\n")
flows = {}
for line in flow_text.splitlines():
    name, body = re.match(r"(\w+)\{(.*)\}", line).groups()
    flows[name] = body.split(",")


def accepted(part):
    name = "in"
    while name not in "AR":
        for rule in flows[name]:
            if ":" not in rule:
                name = rule
                break
            test, target = rule.split(":")
            value, limit = part[test[0]], int(test[2:])
            if (value < limit) if test[1] == "<" else (value > limit):
                name = target
                break
    return name == "A"


total = 0
for line in part_text.splitlines():
    part = {k: int(v) for k, v in re.findall(r"(\w)=(\d+)", line)}
    if accepted(part):
        total += sum(part.values())
print(total)
