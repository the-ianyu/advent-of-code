from os import path

filename = "scratchcards.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [[[int(z) for z in y.split()] for y in x[x.find(":")+2:].split("|")] for x in f.read().splitlines()]

total = 0
for i in content:
    total += int(2 ** (sum(i[1][j] in i[0] for j in range(len(i[1])))-1))
print("Part 1:", total)
