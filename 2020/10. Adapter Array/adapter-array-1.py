import os

filename = "adapter-array.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = sorted([int(x) for x in f.read().splitlines()])
content = [0] + content + [content[-1]+3]

print("Part 1:", 
      sum(content[i]-content[i-1] == 3 for i in range(1, len(content)))*
      sum(content[i]-content[i-1] == 1 for i in range(1, len(content))))
