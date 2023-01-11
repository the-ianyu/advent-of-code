import os

filename = "report-repair.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

for i in content:
    for j in content:
        for k in content:
            if int(i) + int(j) + int(k) == 2020:
                p2 = int(i) * int(j) * int(k)
print("Part 2:", p2)