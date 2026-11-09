import sys

lines = sys.stdin.read().split("\n")
blocks = [lines[i:i + 18] for i in range(0, 252, 18)]
stack, digits = [], [0] * 14
for i, block in enumerate(blocks):
    if block[4].endswith(" 1"):
        stack.append((i, int(block[15].split()[-1])))
    else:
        j, add = stack.pop()
        diff = add + int(block[5].split()[-1])
        digits[j] = min(9, 9 - diff)
        digits[i] = digits[j] + diff
print("".join(map(str, digits)))
