import os, time

filename = "regolith-reservoir.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

start_time = time.time()
with open(filepath, "r") as f:
    content = f.read().splitlines()
content.append("0,173 -> 1000,173")
x_axis = []
grid = []
lowest_point = 0
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
                    if temp[j][0] not in x_axis:
                        x_axis.append(temp[j][0])
                    if k > lowest_point:
                        lowest_point = k
            elif temp[j+1][1] < temp[j][1]:
                for k in range(temp[j+1][1], temp[j][1]+1):
                    if [temp[j][0], k] not in grid:
                        grid.append([temp[j][0], k])
                    if temp[j][0] not in x_axis:
                        x_axis.append(temp[j][0])
                    if k > lowest_point:
                        lowest_point = k
        elif temp[j+1][1] == temp[j][1]:
            if temp[j+1][0] > temp[j][0]:
                for k in range(temp[j][0], temp[j+1][0]+1):
                    if [k, temp[j][1]] not in grid:
                        grid.append([k, temp[j][1]])
                    if k not in x_axis:
                        x_axis.append(k)
                    if temp[j][1] > lowest_point:
                        lowest_point = temp[j][1]
            elif temp[j+1][0] < temp[j][0]:
                for k in range(temp[j+1][0], temp[j][0]+1):
                    if [k, temp[j][1]] not in grid:
                        grid.append([k, temp[j][1]])
                    if k not in x_axis:
                        x_axis.append(k)
                    if temp[j][1] > lowest_point:
                        lowest_point = temp[j][1]
sand_location = [500, 0]
sandTotal = 0
loopran = 1
i = 0
timer = 60
while loopran:
    if time.time()-start_time > timer:
        if timer == 60:
            print(f"{timer//60} minute elapsed. {sandTotal} sand grains have fallen.")
            timer += 60
        else:
            print(f"{timer//60} minutes elapsed. {sandTotal} sand grains have fallen.")
            timer += 60
    if i == 0:
        loopran = 0
    if sand_location[0] not in x_axis:
        break
    elif sand_location[1] > lowest_point:
        break
    if [sand_location[0], sand_location[1]+1] not in grid:
        sand_location[1] += 1
        loopran = 1
        i = 1
        continue
    elif [sand_location[0]-1, sand_location[1]+1] not in grid:
        sand_location[0] -= 1
        sand_location[1] += 1
        loopran = 1
        i = 1
        continue
    elif [sand_location[0]+1, sand_location[1]+1] not in grid:
        sand_location[0] += 1
        sand_location[1] += 1
        loopran = 1
        i = 1
        continue
    grid.append(sand_location[:])
    sand_location = [500, 0]
    sandTotal += 1
    i = 0
print("Part 2:", sandTotal)
print(f"Time elapsed: {round(time.time()-start_time, 2)} minutes.")