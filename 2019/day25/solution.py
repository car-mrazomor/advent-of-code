import re
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from intcode import Intcode

BACK = {"north": "south", "south": "north", "east": "west", "west": "east"}
DANGER = {"infinite loop", "giant electromagnet", "molten lava", "escape pod", "photons"}

droid = Intcode.load(sys.stdin.read())


def say(command=None):
    return "".join(map(chr, droid.run(*map(ord, command + "\n")) if command else droid.run()))


def listed(text, title):
    match = re.search(title + r":\n((?:- .+\n)+)", text)
    return re.findall(r"- (.+)", match[1]) if match else []


rooms, route = set(), {}


def explore(text, path):
    name = re.findall(r"== (.+) ==", text)[-1]
    if name in rooms:
        return
    rooms.add(name)
    for item in listed(text, "Items here"):
        if item not in DANGER:
            say("take " + item)
    if name == "Security Checkpoint":
        route["path"] = list(path)
        route["floor"] = next(d for d in listed(text, "Doors here lead") if not path or d != BACK[path[-1]])
        return
    for door in listed(text, "Doors here lead"):
        if path and door == BACK[path[-1]]:
            continue
        explore(say(door), path + [door])
        say(BACK[door])


explore(say(), [])
for step in route["path"]:
    say(step)
items = listed(say("inv"), "Items in your inventory")
for item in items:
    say("drop " + item)
held = set()
for size in range(len(items) + 1):
    for combo in combinations(items, size):
        for item in held - set(combo):
            say("drop " + item)
        for item in set(combo) - held:
            say("take " + item)
        held = set(combo)
        result = say(route["floor"])
        if "Alert!" not in result:
            print(re.search(r"(\d+) on the keypad", result)[1])
            sys.exit()
