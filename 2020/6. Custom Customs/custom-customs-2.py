import os
from string import ascii_lowercase as letters

filename = "custom-customs.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split("\n") for x in f.read().split("\n\n")]

total = 0
for i in content:
    for j in letters:
        total += 1 if all(j in x for x in i) else 0
print("Part 2:", total)