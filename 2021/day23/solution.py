import heapq
import sys

COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
DOORS = [2, 4, 6, 8]
STOPS = [0, 1, 3, 5, 7, 9, 10]

lines = sys.stdin.read().splitlines()
rooms = tuple("".join(line[3 + 2 * r] for line in lines[2:-1] if len(line) > 3 + 2 * r and line[3 + 2 * r] in COST)
              for r in range(4))
depth = len(rooms[0])
goal = ("." * 11, tuple(c * depth for c in "ABCD"))


def moves(hall, rooms):
    for h, who in enumerate(hall):
        if who == ".":
            continue
        r = "ABCD".index(who)
        if any(c != who for c in rooms[r]):
            continue
        door = DOORS[r]
        if any(hall[i] != "." for i in range(min(h, door), max(h, door) + 1) if i != h):
            continue
        steps = abs(h - door) + depth - len(rooms[r])
        new_rooms = rooms[:r] + (who + rooms[r],) + rooms[r + 1:]
        yield steps * COST[who], hall[:h] + "." + hall[h + 1:], new_rooms
    for r, room in enumerate(rooms):
        if not room or all(c == "ABCD"[r] for c in room):
            continue
        who, door = room[0], DOORS[r]
        for h in STOPS:
            if any(hall[i] != "." for i in range(min(h, door), max(h, door) + 1)):
                continue
            steps = abs(h - door) + depth - len(room) + 1
            new_rooms = rooms[:r] + (room[1:],) + rooms[r + 1:]
            yield steps * COST[who], hall[:h] + who + hall[h + 1:], new_rooms


start = ("." * 11, rooms)
best = {start: 0}
heap = [(0, start)]
while heap:
    energy, state = heapq.heappop(heap)
    if state == goal:
        print(energy)
        break
    if energy > best[state]:
        continue
    for cost, hall, new_rooms in moves(*state):
        nxt = (hall, new_rooms)
        if energy + cost < best.get(nxt, 1 << 60):
            best[nxt] = energy + cost
            heapq.heappush(heap, (energy + cost, nxt))
