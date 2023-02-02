import os

filename = "handheld-halting.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

def main(local_content):
    local_accumulator, index, used = 0, 0, []
    while True:
        if index in used:
            return False, local_accumulator
        used.append(index)
        match local_content[index].split():
            case ["acc", value]:
                local_accumulator += int(value)
                index += 1
            case ["jmp", value]:
                index += int(value)
            case ["nop", value]:
                index += 1
        if index == len(content)-1:
            return True, local_accumulator

for x in range(len(content)):
    if (cmd := content[x].split())[0] == "nop":
        result, accumulator = main(content[:x] + ["jmp " + cmd[1]] + content[x+1:])
        if result:
            break
    elif (cmd := content[x].split())[0] == "jmp":
        result, accumulator = main(content[:x] + ["nop " + cmd[1]] + content[x+1:])
        if result:
            break
print("Part 2:", accumulator)