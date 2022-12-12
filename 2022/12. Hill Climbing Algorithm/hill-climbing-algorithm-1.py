from os import path as p
from string import ascii_lowercase as letters

filename = "hill-climbing-algorithm.txt"
here = p.dirname(p.abspath(__file__))
filepath = p.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

letters = "S" + letters + "E"
horlen, verlen = len(content[0]), len(content)

elevations, startpoints= [], []
for i in range(0, verlen):
    elevations.append([])
    for j in range(0, horlen):
        if content[i][j] == "S":
            start = [i, j]
        if content[i][j] == "E":
            end = [i, j]
        elevations[i].append(content[i][j])

def getNeighbors(x, y, c):
    neighbors = []
    if x+1 < verlen:
        if letters.index(elevations[x+1][y]) - letters.index(elevations[x][y]) <= 1:
            neighbors.append((x+1, y, c))
    if y+1 < horlen:
        if letters.index(elevations[x][y+1]) - letters.index(elevations[x][y]) <= 1:
            neighbors.append((x, y+1, c))
    if x > 0:
        if letters.index(elevations[x-1][y]) - letters.index(elevations[x][y]) <= 1:
            neighbors.append((x-1, y, c))
    if y > 0:
        if letters.index(elevations[x][y-1]) - letters.index(elevations[x][y]) <= 1:
            neighbors.append((x, y-1, c))
    return neighbors

def bfs(x, y):
    queue = [(x, y, 1)]
    while len(queue) > 0:
        v = queue.pop(0)
        if not marked[v[0]][v[1]]:
            marked[v[0]][v[1]] = not marked[v[0]][v[1]]
            for w in getNeighbors(v[0], v[1], v[2]):
                if not marked[w[0]][w[1]]:
                    queue.append((w[0], w[1], w[2]+1))
                    if [w[0], w[1]] == end:
                        return w[2]
    return float("inf")

marked = [[False for _ in range(horlen)] for _ in range(verlen)]
print("Part 1:", bfs(start[0], start[1]))