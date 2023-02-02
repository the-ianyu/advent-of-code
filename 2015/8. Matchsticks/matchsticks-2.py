import os

filename = "matchsticks.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

print("Part 2:", sum(len(repr(x))+x.count('"')-len(x) for x in content))