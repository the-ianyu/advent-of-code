import os

filename = "binary-diagnostic.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

strlen = len(content[0])
masterlist = [0 for _ in range(strlen)]
b_n = 0
for i in range(0, len(content)):
    for j in range(0, strlen):
        if content[i][j] == "1":
            masterlist[j] += 1
for i in range(0, strlen):
    if (masterlist[i])/(len(content)) > 0.5:
        b_n += 2**(strlen-(i+1))
print(b_n*(2**strlen-(b_n+1)))