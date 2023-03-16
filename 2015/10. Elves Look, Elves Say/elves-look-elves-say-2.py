import os
from itertools import groupby

filename = "elves-look-elves-say.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

def looksay(line):
    return "".join(str(len(list(y)))+str(x) for x, y in groupby(line))

for i in range(50):
    content = looksay(content)
print("Part 2:", len(content))