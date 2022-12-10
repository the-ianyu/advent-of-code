import os

filename = "tuning-trouble.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

def func(distinct):
    for i in range(distinct-1, len(content)):
        templst = [content[i-x] for x in range(distinct)]
        if templst == list(dict.fromkeys(templst)):
            return i+1
print("Part 1:", func(4))
print("Part 2:", func(14))