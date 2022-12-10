import os

filename = "cathode-ray-tube.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

register = 1
signalstrengths, finalstr = [], []
crtstr, crtpos = "", 0

def spriteStringGen(registervalue):
    return "."*(registervalue-1)+"###"+"."*(38-registervalue if registervalue > 0 else 37)

def crt():
    global crtstr, crtpos, finalstr
    crtstr += spritestring[crtpos]
    crtpos += 1
    if crtpos >= 40:
        finalstr.append(crtstr.replace(".", " ").replace("#", "█"))
        crtstr, crtpos = "", 0

spritestring = spriteStringGen(register)
for i in range(0, len(content)):
    if content[i][:4] == "addx":
        for _ in range(0, 2): 
            crt()
            signalstrengths.append(register)
        register += int(content[i][5:])
        spritestring = spriteStringGen(register)
    elif content[i] == "noop":
        crt()
        signalstrengths.append(register)

total, cycles = 0, [20, 60, 100, 140, 180, 220]
for i in range(0, 6):
    total += (signalstrengths[cycles[i]-1]*cycles[i])
print("Part 1:", total)
print("Part 2:")
[print(x) for x in finalstr]