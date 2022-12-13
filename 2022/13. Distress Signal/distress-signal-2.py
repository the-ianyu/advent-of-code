from os import path as p
from ast import literal_eval as lit

filename = "distress-signal.txt"
here = p.dirname(p.abspath(__file__))
filepath = p.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

def recur(leftside, rightside):
    if type(leftside) == int and type(rightside) == int:
        if leftside < rightside:
            return True
        elif leftside > rightside:
            return False
        elif leftside == rightside:
            return None
    if type(leftside) == int:
        leftside = [leftside]
    elif type(rightside) == int:
        rightside = [rightside]
    for comp1, comp2 in zip(leftside, rightside):
        result = recur(comp1, comp2)
        if type(result) == bool:
            return result
    if len(leftside) < len(rightside):
        return True
    elif len(leftside) > len(rightside):
        return False
    elif len(leftside) == len(rightside):
        return None

packets = [lit(content[i]) for i in range(0, len(content)) if content[i] != ""]
packets.append([[2]])
packets.append([[6]])

swapped = True
while swapped:
    swapped = False
    for i in range(0, len(packets)-1):
        if recur(packets[i], packets[i+1]) is False:
            temp = packets[i]
            packets[i] = packets[i+1]
            packets[i+1] = temp
            swapped = True
print("Part 2:", (packets.index([[2]])+1)*(packets.index([[6]])+1))