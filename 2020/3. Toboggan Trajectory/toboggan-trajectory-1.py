import os

filename = "toboggan-trajectory.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

total = 0
for i in range(0, len(content)):
    if content[i][(i*3)%len(content[i])] == "#":
        total += 1
print("Part 1:", total)