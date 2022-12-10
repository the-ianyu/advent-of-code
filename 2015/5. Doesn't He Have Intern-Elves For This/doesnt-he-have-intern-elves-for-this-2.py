import os

filename = "doesnt-he-have-intern-elves-for-this.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

nice = 0
for i in range(0, len(content)):
    pairCount, repCount, lst = 0, 0, []
    for j in range(2, len(content[i])):
        if content[i][j-2] == content[i][j]:
            repCount += 1
        lst.append(content[i][j-2:j])
    lst.append(content[i][-2:])
    for j in range(0, len(lst)):
        for k in range(0, j):
            if j != k+1 and k != j+1 and lst[j] == lst[k]:
                pairCount += 1
    if pairCount >= 1 and repCount >= 1:
        nice += 1
print(nice)