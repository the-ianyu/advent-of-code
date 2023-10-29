import os

filename = "adapter-array.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = sorted([[int(x), 0] for x in f.read().splitlines()], key=lambda x: x[0])

content.insert(0, [0, 1])
for i in range(1, len(content)):
    for j in range(min(i, 3)):
        if content[i][0] - content[i-j-1][0] <= 3:
            content[i][1] += content[i-j-1][1]

print("Part 2:", content[-1][1])
