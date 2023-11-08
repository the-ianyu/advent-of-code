import os

filename = "lanternfish.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [int(x) for x in f.read().split(",")]

total = len(content)
days = 80
for i in content:
    c = [0 for _ in range(9)]
    c[i] = 1
    for j in range(days):
        total += c[0]
        c = [c[1], c[2], c[3], c[4], c[5], c[6], c[0]+c[7], c[8], c[0]]
print("Part 1:", total)
