from os import path

filename = "mirage-maintenance.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

def next_term(polynomial):
    sequences = [polynomial]
    while len(sequences[-1]) > 1:
        sequences.append([sequences[-1][i]-sequences[-1][i-1] for i in range(1, len(sequences[-1]))])
    return sum([x[-1] for x in sequences])

print("Part 2:", sum([next_term([int(x) for x in line.split()][::-1]) for line in content]))
