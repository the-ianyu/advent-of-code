import os, re

filename = "let-it-snow.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [int(x) for x in re.findall(r'\d+', f.read())]

def position(x: int, y: int) -> int:
    return ((x+y-1)*(x+y)//2)-x+1

def algorithm(x: int) -> int:
    return x*252533%33554393

code = 20151125
for _ in range(position(*content)-1):
    code = algorithm(code)
print("Part 1:", code)
