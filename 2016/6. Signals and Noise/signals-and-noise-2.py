import os

filename = "signals-and-noise.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

print("Part 2:", end=" ")
for i in range(len(content[0])):
    counterarray = [0 for _ in range(26)]
    for j in range(len(content)):
        counterarray[ord(content[j][i])-97] += 1
    print(chr(counterarray.index(min(counterarray))+97), end="")
