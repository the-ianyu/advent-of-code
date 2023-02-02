import os

filename = "custom-customs.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.replace("\n", "") for x in f.read().split("\n\n")]

print("Part 1:", sum([len(set(x)) for x in content]))