import os

filename = "tuning-trouble.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

distinct = 4
for i in range(distinct-1, len(content)):
    templst = [content[i-x] for x in range(distinct)]
    if templst == list(dict.fromkeys(templst)):
        print("Part 1:", i+1)
        break