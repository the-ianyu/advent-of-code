import os
from itertools import permutations

filename = "all-in-a-single-night.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

graph, vertices = {}, []
for x in content:
    if not x[0] in graph:
        graph[x[0]] = {}
        vertices.append(x[0])
    graph[x[0]][x[2]] = int(x[4])
    if not x[2] in graph:
        graph[x[2]] = {}
        vertices.append(x[2])
    graph[x[2]][x[0]] = int(x[4])

minpath, maxpath = float("inf"), 0
for i in permutations(range(0, len(graph))):
    currentpath = 0
    i = [vertices[x] for x in list(i)]
    for j in range(1, len(i)):
        currentpath += graph[i[j]][i[j-1]]
    minpath = min(minpath, currentpath)
    maxpath = max(maxpath, currentpath)
print("Part 1:", minpath)
print("Part 2:", maxpath)