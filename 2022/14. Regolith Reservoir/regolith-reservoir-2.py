import os

filename = "regolith-reservoir.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

x_axis, grid, lowest_point = set(), set(), 0
for i in range(0, len(content)):
    temp = content[i].split(" -> ")
    for j in range(0, len(temp)):
        temp[j] = [int(x) for x in temp[j].split(",") ]
    for j in range(0, len(temp)-1):
        if temp[j+1][0] == temp[j][0]:
            if temp[j][1] < temp[j+1][1]:
                for k in range(temp[j][1], temp[j+1][1]+1):
                    if (temp[j][0], k) not in grid:
                        grid.add((temp[j][0], k))
                    if k > lowest_point:
                        lowest_point = k
            elif temp[j][1] > temp[j+1][1]:
                for k in range(temp[j+1][1], temp[j][1]+1):
                    if (temp[j][0], k) not in grid:
                        grid.add((temp[j][0], k))
                    if k > lowest_point:
                        lowest_point = k
        elif temp[j][1] == temp[j+1][1]:
            if temp[j][0] < temp[j+1][0]:
                for k in range(temp[j][0], temp[j+1][0]+1):
                    if (k, temp[j][1]) not in grid:
                        grid.add((k, temp[j][1]))
                    if k not in x_axis:
                        x_axis.add(k)
            elif temp[j][0] > temp[j+1][0]:
                for k in range(temp[j+1][0], temp[j][0]+1):
                    if (k, temp[j][1]) not in grid:
                        grid.add((k, temp[j][1]))
                    if k not in x_axis:
                        x_axis.add(k)

lowest_point += 2
for i in range(500-lowest_point, 500+lowest_point+1):
    grid.add((i, lowest_point))
    if i not in x_axis:
        x_axis.add(i)

sand_location = [500, 0]
sandTotal = 0
while sand_location[0] in x_axis and sand_location[1] <= lowest_point:
    if (sand_location[0], sand_location[1]+1) not in grid:
        sand_location[1] += 1
        continue
    elif (sand_location[0]-1, sand_location[1]+1) not in grid:
        sand_location[0] -= 1
        sand_location[1] += 1
        continue
    elif (sand_location[0]+1, sand_location[1]+1) not in grid:
        sand_location[0] += 1
        sand_location[1] += 1
        continue
    if sand_location == [500,0]:
        sandTotal += 1
        break
    grid.add(tuple(sand_location))
    sand_location = [500, 0]
    sandTotal += 1
print("Part 2:", sandTotal)