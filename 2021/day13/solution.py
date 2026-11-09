import re
import sys

dots_text, folds = sys.stdin.read().split("\n\n", 1)
dots = {tuple(map(int, line.split(","))) for line in dots_text.split()}
axis, line = re.search(r"fold along (\w)=(\d+)", folds).groups()
line = int(line)
if axis == "x":
    dots = {(line - abs(x - line), y) for x, y in dots}
else:
    dots = {(x, line - abs(y - line)) for x, y in dots}
print(len(dots))
