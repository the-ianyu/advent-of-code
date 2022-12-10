import os

filename = "perfectly-spherical-houses-in-a-vacuum.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

robo_current = [0,0]
santa_current = [0,0]
houses = [[0,0]]
try:
    for i in range(0, len(content), 2):
        match content[i]:
            case ">": robo_current[0] += 1
            case "<": robo_current[0] -= 1
            case "^": robo_current[1] += 1
            case "v": robo_current[1] -= 1
        if robo_current not in houses:
            houses.append(robo_current[:])
        match content[i+1]:
            case ">": santa_current[0] += 1
            case "<": santa_current[0] -= 1
            case "^": santa_current[1] += 1
            case "v": santa_current[1] -= 1
        if santa_current not in houses:
            houses.append(santa_current[:])
except:
    pass
print(len(houses))