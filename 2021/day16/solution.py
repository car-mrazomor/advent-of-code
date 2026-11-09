import sys

bits = "".join(f"{int(c, 16):04b}" for c in sys.stdin.read().strip())


def versions(pos):
    total = int(bits[pos:pos + 3], 2)
    kind = int(bits[pos + 3:pos + 6], 2)
    pos += 6
    if kind == 4:
        while bits[pos] == "1":
            pos += 5
        return total, pos + 5
    if bits[pos] == "0":
        length = int(bits[pos + 1:pos + 16], 2)
        pos += 16
        end = pos + length
        while pos < end:
            v, pos = versions(pos)
            total += v
    else:
        count = int(bits[pos + 1:pos + 12], 2)
        pos += 12
        for _ in range(count):
            v, pos = versions(pos)
            total += v
    return total, pos


print(versions(0)[0])
