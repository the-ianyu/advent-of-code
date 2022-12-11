import os

filename = "monkey-in-the-middle.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

monkeyItems = [[[int(x) for x in (content[y][18:]).split(", ")] for y in range(1, len(content), 7)]][0]
monkeyOperations = [(content[x][23:]) for x in range(2, len(content), 7)]
monkeyTest = [int(content[x][21:]) for x in range(3, len(content), 7)]
monkeyConditions = [[int(content[x][29:]), int(content[x+1][30:])] for x in range(4, len(content), 7)]
monkeyInspections = [0 for _ in range(len(monkeyTest))]

modulo = 1
for i in monkeyTest:
    modulo *= i

for _ in range(0, 10000):
    for i in range(0, len(monkeyInspections)):
        for j in range(0, len(monkeyItems[i])):
            current = monkeyItems[i][j]
            if monkeyOperations[i] == "* old":
                current *= current
            elif monkeyOperations[i][:2] == "* ":
                current *= int(monkeyOperations[i][2:])
            elif monkeyOperations[i][:2] == "+ ":
                current += int(monkeyOperations[i][2:])
            current %= modulo
            if current % monkeyTest[i] == 0:
                monkeyItems[monkeyConditions[i][0]].append(current)
            else:
                monkeyItems[monkeyConditions[i][1]].append(current)
            monkeyInspections[i] += 1
        monkeyItems[i] = []
print("Part 2:", sorted(monkeyInspections)[-1]*sorted(monkeyInspections)[-2])