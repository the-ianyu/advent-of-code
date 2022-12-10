import os

filename = "not-quite-lisp.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

floor = 0
for i in range(0, len(content)):
    floor = floor+1 if content[i] == "(" else floor-1
    if floor == -1:
        print(i+1)
        break