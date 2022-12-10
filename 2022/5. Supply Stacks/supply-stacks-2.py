from os import path as p
from string import ascii_uppercase as letters

filename = "supply-stacks.txt"
here = p.dirname(p.abspath(__file__))
filepath = p.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

initial = content[:content.index("")]
masterlist = [[] for _ in range(int(initial[-1][-2]))]

for i in range(0, len(initial)-1):
    for j in range(0, len(initial[0])):
        if initial[i][j] in letters:
            temp = (j-1)//4
            masterlist[temp].append(initial[i][j])
content = content[content.index("")+1:]

for i in range(0, len(content)):
    temp = content[i].split(" ")
    temp = [int(temp[1]), int(temp[3])-1, int(temp[5])-1]
    templst = (masterlist[temp[1]][:temp[0]])#[::-1]
    masterlist[temp[2]] = (templst + masterlist[temp[2]])
    masterlist[temp[1]] = (masterlist[temp[1]][temp[0]:])
print("Part 2: ", end="")
for i in range(0, len(masterlist)):
    print(masterlist[i][0], end="")