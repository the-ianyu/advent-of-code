import os

filename = "password-philosophy.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

total = 0
for i in range(0, len(content)):
    temp = content[i].split(" ")
    rnge = [int(x) for x in temp[0].split("-")]
    if temp[2].count(temp[1][0]) in range(rnge[0], rnge[1]+1):
        total += 1
print("Part 1:", total)