import sys

rule_text, messages = sys.stdin.read().split("\n\n")
rules = {}
for line in rule_text.splitlines():
    key, body = line.split(": ")
    rules[key] = body.strip('"') if body.startswith('"') else [alt.split() for alt in body.split(" | ")]


def ends(rule, text, start):
    body = rules[rule]
    if isinstance(body, str):
        return {start + 1} if text.startswith(body, start) else set()
    found = set()
    for alternative in body:
        positions = {start}
        for part in alternative:
            positions = {end for p in positions for end in ends(part, text, p)}
        found |= positions
    return found


print(sum(len(m) in ends("0", m, 0) for m in messages.split()))
