import os

filename = "passport-processing.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().split("\n\n")

total = 0
for i in content:
    if all(x in i for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        total += 1
print("Part 1:", total)