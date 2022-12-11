import os

filename = "monkey-in-the-middle.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

monkeyOperations = [(content[x][23:]) for x in range(2, len(content), 7)]
monkeyTest = [int(content[x][21:]) for x in range(3, len(content), 7)]
monkeyConditions = [[int(content[x][29:]), int(content[x+1][30:])] for x in range(4, len(content), 7)]

modulo = 1
for i in monkeyTest:
    modulo *= i

def main(part):
    monkeyInspections = [0 for _ in range(len(monkeyTest))]
    monkeyItems = [[[int(x) for x in (content[y][18:]).split(", ")] for y in range(1, len(content), 7)]][0]
    for _ in range(0, (20 if part == 1 else 10000 if part == 2 else 0)):
        for i in range(0, len(monkeyInspections)):
            for j in range(0, len(monkeyItems[i])):
                current = monkeyItems[i][j]
                if monkeyOperations[i] == "* old":
                    current *= current
                elif monkeyOperations[i][:2] == "* ":
                    current *= int(monkeyOperations[i][2:])
                elif monkeyOperations[i][:2] == "+ ":
                    current += int(monkeyOperations[i][2:])
                current = current // 3 if part == 1 else current % modulo
                if current % monkeyTest[i] == 0:
                    monkeyItems[monkeyConditions[i][0]].append(current)
                else:
                    monkeyItems[monkeyConditions[i][1]].append(current)
                monkeyInspections[i] += 1
            monkeyItems[i] = []
    return sorted(monkeyInspections)[-1]*sorted(monkeyInspections)[-2]

print("Part 1:", main(1))
print("Part 2:", main(2))