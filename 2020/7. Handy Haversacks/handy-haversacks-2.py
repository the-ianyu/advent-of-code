import os

filename = "handy-haversacks.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.replace(" bags", "").replace(" bag", "").replace(" contain ", "|").replace(", ", "|").replace(".", "").split("|") for x in f.read().splitlines()]

bags = {x[0]: x[1:] for x in content}

def count_bags(bag):
    global bags, count
    local_bags = bags[bag]
    for x in range(len(local_bags)):
        if local_bags[x] == "no other":
            continue
        for _ in range(int(local_bags[x][:local_bags[x].find(" ")+1])):
            count += 1
            count_bags(local_bags[x][local_bags[x].find(" ")+1:])
    return count

count = 0
print("Part 2:", count_bags("shiny gold"))