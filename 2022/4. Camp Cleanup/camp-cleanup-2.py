import os

filename = "camp-cleanup.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

overlap = 0
for i in range(0, len(content)):
    tmp = [x.split("-") for x in content[i].split(",")]
    lst0 = [int(x) for x in range(int(tmp[0][0]), int(tmp[0][1])+1)]
    lst1 = [int(x) for x in range(int(tmp[1][0]), int(tmp[1][1])+1)]
    for j in range(0, len(lst0)):
        if lst0[j] in lst1:
            overlap += 1
            break
print("Part 2:", overlap)