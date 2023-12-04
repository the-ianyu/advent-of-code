from os import path

filename = "scratchcards.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [[[int(z) for z in y.split()] for y in x[x.find(":")+2:].split("|")] for x in f.read().splitlines()]

ctr = [1 for _ in range(len(content))]
for i in range(len(content)):
    for j in range(i+1, i+1+sum(content[i][1][j] in content[i][0] for j in range(len(content[i][1])))):
        ctr[j] += ctr[i]
print("Part 2:", sum(ctr))
