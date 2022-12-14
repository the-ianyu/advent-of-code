import os, time

filename = "regolith-reservoir.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

start_time = time.time()
with open(filepath, "r") as f:
    content = f.read().splitlines()

grid = []
for i in range(0, len(content)):
    temp = content[i].split(" -> ")
    for j in range(0, len(temp)):
        temp[j] = [int(x) for x in temp[j].split(",") ]
    for j in range(0, len(temp)-1):
        if temp[j+1][0] == temp[j][0]:
            if temp[j+1][1] > temp[j][1]:
                for k in range(temp[j][1], temp[j+1][1]+1):
                    if [temp[j][0], k] not in grid:
                        grid.append([temp[j][0], k])
            elif temp[j+1][1] < temp[j][1]:
                for k in range(temp[j+1][1], temp[j][1]+1):
                    if [temp[j][0], k] not in grid:
                        grid.append([temp[j][0], k])
        elif temp[j+1][1] == temp[j][1]:
            if temp[j+1][0] > temp[j][0]:
                for k in range(temp[j][0], temp[j+1][0]+1):
                    if [k, temp[j][1]] not in grid:
                        grid.append([k, temp[j][1]])
            elif temp[j+1][0] < temp[j][0]:
                for k in range(temp[j+1][0], temp[j][0]+1):
                    if [k, temp[j][1]] not in grid:
                        grid.append([k, temp[j][1]])
x_axis = []
for i in range(0, len(grid)):
    if grid[i][0] not in x_axis:
        x_axis.append(grid[i][0])
lowest_points = []
for i in range(0, len(x_axis)):
    lowest_points.append([x_axis[i], 0])
    for j in range(0, len(grid)):
        if grid[j][0] == x_axis[i]:
            if grid[j][1] > lowest_points[i][1]:
                lowest_points[i][1] = grid[j][1]
sand_location = [500, 0]
i = 0
while True:
    if sand_location[0] not in x_axis:
        break
    elif sand_location[1] > lowest_points[x_axis.index(sand_location[0])][1]:
        break
    if [sand_location[0], sand_location[1]+1] not in grid:
        sand_location[1] += 1
        continue
    elif [sand_location[0]-1, sand_location[1]+1] not in grid:
        sand_location[0] -= 1
        sand_location[1] += 1
        continue
    elif [sand_location[0]+1, sand_location[1]+1] not in grid:
        sand_location[0] += 1
        sand_location[1] += 1
        continue
    grid.append(sand_location[:])
    sand_location = [500, 0]
    i += 1
print("Part 1:", i)
print(f"Time elapsed: {round((time.time()-start_time)/60, 2)} minutes.")