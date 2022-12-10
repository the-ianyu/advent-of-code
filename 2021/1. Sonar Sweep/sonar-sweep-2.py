import os

filename = "sonar-sweep.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()
    
numbers = [int(n) for n in content]
total = 0
for i in range(3, len(numbers)):
    if numbers[i] > numbers[i-3]:
        total += 1
print(total)