import os

filename = "corporate-policy.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [ord(x) for x in f.read()]

def increment(content: list) -> list:
    content[-1] += 1
    for i in range(len(content)-1, -1, -1):
        if content[i] > 122:
            content[i] = 97
            content[i-1] += 1
        else:
            break
    return content

def approved(content: list) -> bool:
    for i in range(len(content)-2):
        if content[i] == content[i+1]-1 and content[i] == content[i+2]-2:
            break
    else:
        return False
    if 105 in content or 111 in content or 108 in content:
        return False
    ctr = 0
    for i in range(len(content)-1):
        if ctr == 1:
            ctr = 2
            continue
        if content[i] == content[i+1]:
            ctr += 1
        if ctr == 3:
            return True

while not approved(content):
    content = increment(content)

print("Part 1:", "".join(chr(x) for x in content))
