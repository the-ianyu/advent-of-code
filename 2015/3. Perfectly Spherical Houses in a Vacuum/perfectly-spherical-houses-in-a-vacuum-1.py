import os

filename = "perfectly-spherical-houses-in-a-vacuum.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

current = [0,0]
houses = [[0,0]]

for i in range(0, len(content)):
    match content[i]:
        case ">": current[0] += 1
        case "<": current[0] -= 1
        case "^": current[1] += 1
        case "v": current[1] -= 1
    if current not in houses:
        houses.append(current[:])
print(len(houses))