import sys

patterns_text, designs = sys.stdin.read().strip().split("\n\n")
patterns = [p.strip() for p in patterns_text.split(",")]


def possible(design):
    ok = [True] + [False] * len(design)
    for i in range(len(design)):
        if ok[i]:
            for p in patterns:
                if design.startswith(p, i):
                    ok[i + len(p)] = True
    return ok[-1]


print(sum(possible(d) for d in designs.split()))
