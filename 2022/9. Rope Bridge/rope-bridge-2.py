import os

filename = "rope-bridge.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

visited_locations = [[0, 0]]
rope = [[0, 0] for _ in range(10)]

def main(head_location, tail_location):
    if abs(tail_location[0] - head_location[0]) == 2:
        tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
        if abs(tail_location[1] - head_location[1]) >= 1:
            tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
    elif abs(tail_location[1] - head_location[1]) == 2:
        tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
        if abs(tail_location[0] - head_location[0]) >= 1:
            tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
    return tail_location

for i in range(0, len(content)):
    for j in range(0, int(content[i][2:])):
        if content[i][0] == "U":
            rope[0][1] += 1
        elif content[i][0] == "D":
            rope[0][1] -= 1
        elif content[i][0] == "L":
            rope[0][0] -= 1
        elif content[i][0] == "R":
            rope[0][0] += 1
        for k in range(1, 10):
            rope[k] = main(rope[k-1], rope[k])
        if rope[9] not in visited_locations:
            visited_locations.append(rope[9][:])
print("Part 2:", len(visited_locations))