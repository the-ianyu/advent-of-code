from os import path
from re import findall
from math import prod

filename = "cube-conundrum.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split(" ")[2:] for x in f.read().splitlines()]

total = 0
for i in content:
    roundcount = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    bestcount = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for j in range(0, len(i), 2):
        roundcount[''.join(findall('[a-z]', i[j+1]))] += int(i[j])
        if ";" in i[j+1] or j == len(i) - 2:
            for k in roundcount:
                bestcount[k] = max(bestcount[k], roundcount[k])
                roundcount[k] = 0
    total += prod(bestcount.values())
print("Part 2:", total)
