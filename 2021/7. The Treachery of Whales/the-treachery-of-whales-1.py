import os

filename = "the-treachery-of-whales.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = sorted([int(x) for x in f.read().split(",")])

minimum = float("inf")
for i in range(content[0], content[-1]):
    temp = 0
    for j in range(len(content)):
        temp += abs(i - content[j])
    minimum = min(minimum, temp)
print(minimum)
