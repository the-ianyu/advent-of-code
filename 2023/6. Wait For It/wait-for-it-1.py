from os import path

filename = 'wait-for-it.txt'
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, 'r') as f:
    content = tuple((int(x[0]), int(x[1])) for x in list(zip(*(x.split() for x in f.read().splitlines())))[1:])

total = 1
for i in content:
    r = 0
    for j in range(i[0]):
        if j * (i[0]-j )> i[1]:
            r += 1
    total *= r
print("Part 1:", total)
