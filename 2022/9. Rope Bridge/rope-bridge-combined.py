import os

filename = "rope-bridge.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

visited_locations_1, visited_locations_2 = [[0, 0]], [[0, 0]]
rope = [[0, 0] for _ in range(10)]

def main(head_location, tail_location): # both methods work
    if True:
        if abs(tail_location[0] - head_location[0]) == 2:
            tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
            if abs(tail_location[1] - head_location[1]) >= 1:
                tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
        elif abs(tail_location[1] - head_location[1]) == 2:
            tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
            if abs(tail_location[0] - head_location[0]) >= 1:
                tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
    if False:
        if tail_location[0] - head_location[0] == 2:
            tail_location[0] -= 1
            if tail_location[1] - head_location[1] >= 1:
                tail_location[1] -= 1
            elif tail_location[1] - head_location[1] <= -1:
                tail_location[1] += 1
        elif tail_location[0] - head_location[0] == -2:
            tail_location[0] += 1
            if tail_location[1] - head_location[1] >= 1:
                tail_location[1] -= 1
            elif tail_location[1] - head_location[1] <= -1:
                tail_location[1] += 1
        elif tail_location[1] - head_location[1] == 2:
            tail_location[1] -= 1
            if tail_location[0] - head_location[0] >= 1:
                tail_location[0] -= 1
            elif tail_location[0] - head_location[0] <= -1:
                tail_location[0] += 1
        elif tail_location[1] - head_location[1] == -2:
            tail_location[1] += 1
            if tail_location[0] - head_location[0] >= 1:
                tail_location[0] -= 1
            elif tail_location[0] - head_location[0] <= -1:
                tail_location[0] += 1
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
        if rope[1] not in visited_locations_1:
            visited_locations_1.append(rope[1][:])
        if rope[9] not in visited_locations_2:
            visited_locations_2.append(rope[9][:])
print("Part 1:", len(visited_locations_1))
print("Part 2:", len(visited_locations_2))