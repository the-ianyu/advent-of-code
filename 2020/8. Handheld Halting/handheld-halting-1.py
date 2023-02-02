import os

filename = "handheld-halting.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

accumulator, index, used = 0, 0, []
while True:
    if index in used:
        break
    used.append(index)
    match content[index].split():
        case ["acc", value]:
            accumulator += int(value)
            index += 1
        case ["jmp", value]:
            index += int(value)
        case ["nop", value]:
            index += 1
print("Part 1:", accumulator)