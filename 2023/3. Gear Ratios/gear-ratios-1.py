from os import path
from string import punctuation

filename = "gear-ratios.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [[y for y in x] for x in f.read().splitlines()]

symbols = punctuation.replace(".", "")
horlen = len(content[0])
verlen = len(content)

def partnumber_check(start, end, symbols):
    if start[1]-1 >= 0:
        if content[start[0]][start[1]-1] in symbols:
            return True
    if end[1]+1 < horlen:
        if content[end[0]][end[1]+1] in symbols:
            return True
    for i in range(start[1]-1, end[1]+2):
        if start[0]-1 >= 0 and i < horlen:
            if content[start[0]-1][i] in symbols:
                return True
        if end[0]+1 < verlen and i < horlen:
            if content[end[0]+1][i] in symbols:
                return True
    return False

total = 0
numberflag = False
numstr = ""
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
            if partnumber_check(start, end, symbols):
                total += int(numstr)
            numstr = ""
print("Part 1:", total)
