import os

filename = "giant-squid.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()
    drawn = [int(x) for x in content[0].split(",")]
    boards = [[[int(y) for y in x.split()] for x in content[i:i+5]] for i in range(2, len(content), 6)]

def getscore(board, drawn):
    sums = [drawn[-1], 0]
    for i in board:
        for j in i:
            if j not in drawn:
                sums[1] += j
    return sums[0] * sums[1]

complete = 0
for i in range(5, len(drawn)):
    for j in boards:
        if complete:
            break
        for k in range(5):
            if all(j[k][l] in drawn[:i] for l in range(5)):
                complete = getscore(j, drawn[:i])
        for k in range(5):
            if all(j[l][k] in drawn[:i] for l in range(5)):
                complete = getscore(j, drawn[:i])
    else:
        continue
    break

print(complete)
