import sys

rule_text, update_text = sys.stdin.read().strip().split("\n\n")
before = {tuple(line.split("|")) for line in rule_text.split()}
total = 0
for line in update_text.split():
    pages = line.split(",")
    if all((b, a) not in before for i, a in enumerate(pages) for b in pages[i + 1:]):
        total += int(pages[len(pages) // 2])
print(total)
