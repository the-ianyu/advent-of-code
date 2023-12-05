import os, re

filename = "jsabacusframework-io.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    print("Part 1:", sum([int(x) for x in re.findall(r'-?\d+', f.read())]))
