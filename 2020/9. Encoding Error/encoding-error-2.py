import os

filename = "encoding-error.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [int(x) for x in f.read().splitlines()]

preamble_length = 25
content_copy = content[:]
preamble = content[:preamble_length]
content = content[preamble_length:]

for x in content:
    for y in preamble:
        for z in preamble:
            if y + z == x:
                preamble.pop(0)
                preamble.append(x)
                break
        else:
            continue
        break
    else:
        invalid = x
        break

content = content_copy[:]
for i in range(2, len(content)+1):
    for j in range(len(content)-i+1):
        if sum(temp := content[j:j+i]) == int(invalid):
            print("Part 2:", min(temp)+max(temp))
            break
    else:
        continue
    break