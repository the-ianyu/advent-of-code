import os

filename = "cathode-ray-tube.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

register = 1
signalstrengths = []

for i in range(0, len(content)):
    if content[i][:4] == "addx":
        for _ in range(0, 2): signalstrengths.append(register)
        register += int(content[i][5:])
    elif content[i] == "noop":
        signalstrengths.append(register)

total, cycles = 0, [20, 60, 100, 140, 180, 220]
for i in range(0, 6):
    total += (signalstrengths[cycles[i]-1]*cycles[i])
print("Part 1:", total)