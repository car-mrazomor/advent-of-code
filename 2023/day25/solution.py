import sys
from collections import defaultdict, deque

graph = defaultdict(set)
for line in sys.stdin.read().splitlines():
    if ":" in line:
        name, others = line.split(":")
        for other in others.split():
            graph[name].add(other)
            graph[other].add(name)
nodes = list(graph)


def cut_side(source, sink):
    flow = defaultdict(int)
    for _ in range(4):
        parent = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            u = queue.popleft()
            for v in graph[u]:
                if v not in parent and flow[(u, v)] < 1:
                    parent[v] = u
                    queue.append(v)
        if sink not in parent:
            return parent
        v = sink
        while parent[v] is not None:
            u = parent[v]
            flow[(u, v)] += 1
            flow[(v, u)] -= 1
            v = u
    return None


for sink in nodes[1:]:
    side = cut_side(nodes[0], sink)
    if side:
        print(len(side) * (len(nodes) - len(side)))
        break
