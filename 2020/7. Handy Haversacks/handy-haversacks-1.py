import os

filename = "handy-haversacks.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.replace(" bags", "").replace(" bag", "").replace(" contain ", "|").replace(", ", "|").replace(".", "").split("|") for x in f.read().splitlines()]

bags = {x[0]: x[1:] for x in content}

def find_bags(bag):
    global bags
    if bag == "shiny gold":
        return True
    for x in bags[bag]:
        if x != "no other":
            status = find_bags(x[x.find(" ")+1:])
            if status:
                return True
    return False

count = 0
for x in bags:
    if x == "shiny gold":
        continue
    if find_bags(x):
        count += 1
print("Part 1:", count)