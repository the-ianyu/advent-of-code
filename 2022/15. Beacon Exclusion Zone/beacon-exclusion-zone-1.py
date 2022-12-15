import os

filename = "beacon-exclusion-zone.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

currentRow = 2_000_000
beaconLocations, impossibleLocations = set(), set()
for i in range(0, len(content)):
    temp = content[i].split(" ")
    tempSensor = (int(temp[2][2:-1]), int(temp[3][2:-1]))
    tempBeacon = (int(temp[8][2:-1]), int(temp[9][2:]))
    beaconLocations.add(tempBeacon) if tempBeacon[1] == currentRow else None
    tempDistance = sum(abs(x-y) for x, y in zip(tempSensor, tempBeacon))
    endpoint = (tempDistance-abs(tempSensor[1]-currentRow))
    for y in range(tempSensor[0]-endpoint, tempSensor[0]+endpoint+1):
        impossibleLocations.add(y)
print("Part 1:", len(impossibleLocations)-len(beaconLocations))