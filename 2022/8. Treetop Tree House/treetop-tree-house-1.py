import os

filename = "treetop-tree-house.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

horlen, verlen = len(content[0]), len(content)
lst = [[] for _ in range(verlen)]

for i in range(0, verlen):
    for j in range(0, horlen):
        lst[i].append(content[i][j])
    lst[i] = [int(x) for x in lst[i]]

def horfunc(*loop):
    global lst, i, j
    for k in range(loop[0], loop[1], (1 if len(loop) == 2 else loop[2])):
        if lst[k][j] >= lst[i][j]:
            return False
    return True

def verfunc(*loop):
    global lst, i, j
    for k in range(loop[0], loop[1], (1 if len(loop) == 2 else loop[2])):
        if lst[i][k] >= lst[i][j]:
            return False
    return True

total = 0
for i in range(0, horlen):
    for j in range(0, verlen):
        if horfunc(i-1, -1, -1) or horfunc(i+1, horlen):
            total += 1
        elif verfunc(j-1, -1, -1) or verfunc(j+1, verlen):
            total += 1
print("Part 1:", total)