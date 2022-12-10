from os import path as p
from string import ascii_letters as letters

filename = "rucksack-reorganization.txt" 
here = p.dirname(p.abspath(__file__)) 
filepath = p.join(here, filename)

with open(filepath, "r") as f: 
    content = f.read().splitlines()

total = 0 
for i in range(0, len(content), 3): 
    part1, part2, part3 = content[i], content[i+1], content[i+2] 
    for j in range(0, len(part3)): 
        if part3[j] in part1 and part3[j] in part2: 
            total += (letters.index(part3[j]))+1 
            break 
print("Part 2:", total)