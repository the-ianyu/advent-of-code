import os

filename = "rope-bridge.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

visited_locations = [[0, 0]]
head_location, tail_location = [0, 0], [0, 0]

def main(head_location, tail_location):
    if abs(tail_location[0] - head_location[0]) == 2:
        tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
        if abs(tail_location[1] - head_location[1]) >= 1:
            tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
    elif abs(tail_location[1] - head_location[1]) >= 2:
        tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
        if abs(tail_location[0] - head_location[0]) == 1:
            tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
    return tail_location

for i in range(0, len(content)):
    for j in range(0, int(content[i][2:])):
        if content[i][0] == "U":
            head_location[1] += 1
        elif content[i][0] == "D":
            head_location[1] -= 1
        elif content[i][0] == "L":
            head_location[0] -= 1
        elif content[i][0] == "R":
            head_location[0] += 1
        tail_location = main(head_location, tail_location)
        if tail_location not in visited_locations:
            visited_locations.append(tail_location[:])
print("Part 1:", len(visited_locations))