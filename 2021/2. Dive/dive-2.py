import os

filename = "dive.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

horpos, verpos, aim = 0, 0, 0
for i in range(0, len(content)):
    loc = content[i].find(" ")
    if content[i][:loc] == "up":
        aim -= int(content[i][loc+1:])
    elif content[i][:loc] == "down":
        aim += int(content[i][loc+1:])
    else:
        horpos += int(content[i][loc+1:])
        verpos += (int(content[i][loc+1:]) * aim)
print(verpos*horpos)