from os import path

filename = "haunted-wasteland.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

moves = content[0]
mapper = {}

for i in content[2:]:
    i = i.split()
    mapper[i[0]] = {"L": i[2][1:4], "R": i[3][0:3]}

ptr = 0
current = "AAA"
while True:
    move = moves[ptr%len(moves)]
    current = mapper[current][move]
    ptr += 1
    if current == "ZZZ":
        break
print(ptr)
