import os
from math import prod

filename = "toboggan-trajectory.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

total = [0 for _ in range(5)]
for i in range(0, len(content)):
    if content[i][(i*1)%len(content[i])] == "#":
        total[0] += 1
    if content[i][(i*3)%len(content[i])] == "#":
        total[1] += 1
    if content[i][(i*5)%len(content[i])] == "#":
        total[2] += 1
    if content[i][(i*7)%len(content[i])] == "#":
        total[3] += 1
    if content[i][(i//2)%len(content[i])] == "#" and not i % 2:
        total[4] += 1
print("Part 2:", prod(total))