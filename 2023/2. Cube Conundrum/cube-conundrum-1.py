from os import path
from re import findall

filename = "cube-conundrum.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split(" ")[2:] for x in f.read().splitlines()]

limit = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0
for n, i in enumerate(content):
    roundcount = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for j in range(0, len(i), 2):
        roundcount[''.join(findall('[a-z]', i[j+1]))] += int(i[j])
        if ";" in i[j+1] or j == len(i) - 2:
            for k in roundcount:
                if roundcount[k] > limit[k]:
                    break
                roundcount[k] = 0
            else:
                continue
            break
    else:
        total += n+1
print("Part 1:", total)
