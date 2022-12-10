import os

filename = "i-was-told-there-would-be-no-math.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

total = 0
for i in range(0, len(content)):
    active = sorted([int(x) for x in (content[i].split("x"))])
    total += (active[0]*active[1]*active[2]) + (2*active[0]) + (2*active[1])
print(total)