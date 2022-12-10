import os

filename = "camp-cleanup.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

enclosed = 0
for i in range(0, len(content)):
    tmp = [x.split("-") for x in content[i].split(",")]
    if int(tmp[0][0]) < int(tmp[1][0]) and int(tmp[0][1]) >= int(tmp[1][1]):
        enclosed += 1
    elif int(tmp[0][0]) > int(tmp[1][0]) and int(tmp[0][1]) <= int(tmp[1][1]):
        enclosed += 1
    elif int(tmp[0][0]) == int(tmp[1][0]):
        enclosed += 1
print("Part 1:", enclosed)