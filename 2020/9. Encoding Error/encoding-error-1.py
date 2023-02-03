import os

filename = "encoding-error.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

preamble_length = 25
preamble = content[:preamble_length]
content = content[preamble_length:]

for x in content:
    for y in preamble:
        for z in preamble:
            if int(y) + int(z) == int(x):
                preamble.pop(0)
                preamble.append(x)
                break
        else:
            continue
        break
    else:
        print("Part 1:", x)
        break