import os

filename = "hydrothermal-venture.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in f.read().splitlines()]

master = set()
duplicate = set()

for i in content.copy():
    if not (i[0][0] == i[1][0] or i[0][1] == i[1][1]):
        content.remove(i)

diffsolve = lambda num: num - 1 if num > 0 else num + 1 if num < 0 else 0

total = 0
done = 0
for i in (content):
    redo = 1
    xdiff = i[1][0] - i[0][0]
    ydiff = i[1][1] - i[0][1]
    while (xdiff != 0 or ydiff != 0) or redo:
        if (xdiff == 0 and ydiff == 0) and redo:
            redo = 0
        if (i[0][0] + xdiff, i[0][1] + ydiff) not in master:
            master.add((i[0][0] + xdiff, i[0][1] + ydiff))
        else:
            if (i[0][0] + xdiff, i[0][1] + ydiff) not in duplicate:
                duplicate.add((i[0][0] + xdiff, i[0][1] + ydiff))
                total += 1
        xdiff = diffsolve(xdiff)
        ydiff = diffsolve(ydiff)

print("Part 1:", total)
