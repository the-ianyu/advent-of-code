import os

filename = "treetop-tree-house.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

horlen, verlen = len(content[0]), len(content)
lst = [[] for _ in range(horlen)]

for i in range(0, horlen):
    for j in range(0, verlen):
        lst[i].append(content[i][j])
    lst[i] = [int(x) for x in lst[i]]

def horfunc(*loop):
    global lst, i, j
    scenic = 0
    for k in range(loop[0], loop[1], (1 if len(loop) == 2 else loop[2])):
        scenic += 1
        if lst[k][j] >= lst[i][j]:
            return False, scenic
    return True, scenic

def verfunc(*loop):
    global lst, i, j
    scenic = 0
    for k in range(loop[0], loop[1], (1 if len(loop) == 2 else loop[2])):
        scenic += 1
        if lst[i][k] >= lst[i][j]:
            return False, scenic
    return True, scenic

total, maxscore = 0, 0
for i in range(0, horlen):
    for j in range(0, verlen):
        status = [False, False, False, False]
        status[0], scenic1 = horfunc(i-1, -1, -1)
        status[1], scenic2 = horfunc(i+1, horlen)
        status[2], scenic3 = verfunc(j-1, -1, -1)
        status[3], scenic4 = verfunc(j+1, verlen)
        if any(status):
            total += 1
        score = scenic1*scenic2*scenic3*scenic4
        maxscore = score if score > maxscore else maxscore
print("Part 1:", total)
print("Part 2:", maxscore)