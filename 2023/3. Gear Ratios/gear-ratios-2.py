from os import path
from string import punctuation

filename = "gear-ratios.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [[y for y in x] for x in f.read().splitlines()]

horlen = len(content[0])
verlen = len(content)

def partnumber_check(start, end, symbols):
    if start[1]-1 >= 0:
        if content[start[0]][start[1]-1] in symbols:
            return True, (start[0], start[1]-1)
    if end[1]+1 < horlen:
        if content[end[0]][end[1]+1] in symbols:
            return True, (end[0], end[1]+1)
    for i in range(start[1]-1, end[1]+2):
        if start[0]-1 >= 0 and i < horlen:
            if content[start[0]-1][i] in symbols:
                return True, (start[0]-1, i)
        if end[0]+1 < verlen and i < horlen:
            if content[end[0]+1][i] in symbols:
                return True, (end[0]+1, i)
    return False, None

numberflag = False
numstr = ""
gearadjacent = dict()
for i in range(verlen):
    for j in range(horlen):
        if content[i][j].isnumeric():
            if not numberflag:
                start = (i, j)
                numberflag = True
            numstr += content[i][j]
        if (content[i][j] in punctuation or j == horlen-1) and numberflag:
            numberflag = False
            end = (i, j-1)
            state, location = partnumber_check(start, end, "*")
            if state:
                if location not in gearadjacent:
                    gearadjacent[location] = []
                gearadjacent[location].append(int(numstr))
            numstr = ""
print("Part 2:", sum([(gearadjacent[i][0]*gearadjacent[i][1]) for i in gearadjacent if len(gearadjacent[i]) == 2]))
