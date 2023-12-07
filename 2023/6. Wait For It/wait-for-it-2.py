from os import path

filename = "wait-for-it.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    temp = list(zip(*(x.split() for x in f.read().splitlines())))[1:]
    content = ["", ""]
    for x in temp:
        content[0] += x[0]
        content[1] += x[1]
    content = [(tuple(int(x) for x in content))]

total = 1
for i in content:
    r = 0
    for j in range(i[0]):
        if j * (i[0]-j) > i[1]:
            r += 1
    total *= r
print("Part 2:", total)
