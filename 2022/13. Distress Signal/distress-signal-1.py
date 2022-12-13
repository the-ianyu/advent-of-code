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

sum = 0
for i in range(0, len(content), 3):
    leftside, rightside = lit(content[i]), lit(content[i+1])
    if recur(leftside, rightside) is not False:
        sum += (i//3)+1
print("Part 1:", sum)