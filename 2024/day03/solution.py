import re
import sys

print(sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", sys.stdin.read())))
