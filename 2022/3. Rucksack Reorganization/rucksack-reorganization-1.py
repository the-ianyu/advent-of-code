from os import path as p
from string import ascii_letters as letters

filename = "rucksack-reorganization.txt"
here = p.dirname(p.abspath(__file__))
filepath = p.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

total = 0 
for i in range(0, len(content)): 
    part1, part2 = content[i][:(len(content[i])//2)], content[i][(len(content[i])//2):] 
    for j in range(0, len(part1)): 
        if part1[j] in part2: 
            total += (letters.index(part1[j]))+1 
            break 
print("Part 1:", total)