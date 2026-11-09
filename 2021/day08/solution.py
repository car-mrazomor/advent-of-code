import sys

print(sum(len(word) in (2, 3, 4, 7)
          for line in sys.stdin.read().splitlines() if "|" in line
          for word in line.split("|")[1].split()))
