import os

filename = "beacon-exclusion-zone.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

def dist(p, q): 
    return sum(abs(x-y) for x, y in zip(p, q))

currentRow = 2_000_000
boundaries = (0, 4_000_000)

sensorLocations, beaconLocations, impossibleLocations, radiuses = set(), set(), set(), set()
for i in range(0, len(content)):
    temp = content[i].split(" ")
    tempSensor = (int(temp[2][2:-1]), int(temp[3][2:-1]))
    tempBeacon = (int(temp[8][2:-1]), int(temp[9][2:]))
    sensorLocations.add(tempSensor)
    beaconLocations.add(tempBeacon) if tempBeacon[1] == currentRow else None
    tempDistance = dist(tempSensor, tempBeacon)
    radiuses.add((tempSensor[0], tempSensor[1], tempDistance))
    midpoint = (tempDistance-abs(tempSensor[1]-currentRow))
    for y in range(tempSensor[0]-midpoint, tempSensor[0]+midpoint+1):
        impossibleLocations.add(y)
print("Part 1:", len(impossibleLocations)-len(beaconLocations))

positive, negative = set(), set()
for x, y, r in radiuses:
    positive.add(+x+y+r+1)
    positive.add(+x+y-r-1)
    negative.add(-x+y+r+1)
    negative.add(-x+y-r-1)

for x in positive:
    for y in negative:
        intersection = ((x-y)//2, (x+y)//2)
        if intersection[0] in range(*boundaries) and intersection[1] in range(*boundaries):
            for p in sensorLocations:
                for q in radiuses:
                    if p == q[:2] and dist(intersection, p) <= q[2]:
                        break
                else:
                    continue
                break
            else:
                print("Part 2:", (4_000_000*intersection[0])+intersection[1])