import os

filename = "some-assembly-required.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

wires = {}
def checker(i):
    if (str(i[0]).isnumeric() or i[0] in wires) and (str(i[2]).isnumeric() or i[2] in wires):
        if i[0] in wires:
            i[0] = wires[i[0]]
        if i[2] in wires:
            i[2] = wires[i[2]]
        return True, i
    return False, i

def main(wires, content):
    content = [x[:] for x in content]
    while len(wires) < len(content):
        for i in content:
            if i[1] == "AND":
                condition, i = checker(i)
                if condition:
                    wires[i[4]] = int(i[0]) & int(i[2])
            elif i[1] == "OR":
                condition, i = checker(i)
                if condition:
                    wires[i[4]] = int(i[0]) | int(i[2])
            elif i[0] == "NOT":
                if str(i[1]).isnumeric() or i[1] in wires:
                    if i[1] in wires:
                        i[1] = wires[i[1]]
                    wires[i[3]] = int(i[1]) ^ 65535
            elif i[1] == "LSHIFT":
                condition, i = checker(i)
                if condition:
                    wires[i[4]] = int(i[0]) << int(i[2])
            elif i[1] == "RSHIFT":
                condition, i = checker(i)
                if condition:
                    wires[i[4]] = int(i[0]) >> int(i[2])
            else:
                if i[2] not in wires and (str(i[0]).isnumeric() or i[0] in wires):
                    if i[0] in wires:
                        i[0] = wires[i[0]]
                    wires[i[2]] = int(i[0])
    return wires

wires = main(wires, content)
print("Part 1:", wires["a"])