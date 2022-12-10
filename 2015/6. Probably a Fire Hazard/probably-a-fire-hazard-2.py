import os

filename = "probably-a-fire-hazard.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]
brightness = 0

for i in range(0, len(content)):
    if "turn off" in content[i]:
        status = 0
        content[i] = content[i][9:]
    elif "turn on" in content[i]:
        status = 1
        content[i] = content[i][8:]
    elif "toggle" in content[i]:
        status = 2
        content[i] = content[i][7:]
    temp = content[i].split()
    start, end = [int(x) for x in temp[0].split(",")], [int(x) for x in temp[2].split(",")]
    if status == 0:
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if grid[x][y] != 0:
                    grid[x][y] -= 1
    elif status == 1:
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[x][y] += 1
    elif status == 2:
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[x][y] += 2
for x in range(0, len(grid)):
    for y in range(0, len(grid[0])):
        brightness += grid[x][y]
print(brightness)