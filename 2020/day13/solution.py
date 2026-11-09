import sys

lines = sys.stdin.read().split()
earliest = int(lines[0])
buses = [int(b) for b in lines[1].split(",") if b != "x"]
bus = min(buses, key=lambda b: -earliest % b)
print(bus * (-earliest % bus))
