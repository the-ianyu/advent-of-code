import os

filename = "report-repair.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

for i in content:
    for j in content:
        if int(i) + int(j) == 2020:
            p1 = int(i) * int(j)
print("Part 1:", p1)