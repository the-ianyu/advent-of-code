import os

filename = "calorie-counting.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

finalarray, temp = [], 0
for i in range(0, len(content)):
    if content[i] != "":
        temp += int(content[i])
    else:
        finalarray.append(int(temp))
        temp = 0
finalarray.sort()

print("Part 2:", sum(finalarray[-3:]))