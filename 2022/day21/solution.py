import operator
import sys

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
jobs = dict(line.split(": ") for line in sys.stdin.read().splitlines() if ": " in line)


def yell(name):
    job = jobs[name].split()
    if len(job) == 1:
        return int(job[0])
    return OPS[job[1]](yell(job[0]), yell(job[2]))


print(yell("root"))
