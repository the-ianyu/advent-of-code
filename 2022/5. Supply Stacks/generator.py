# https://www.reddit.com/r/adventofcode/comments/zdbvzn

# This generates a valid input file for AOC 2022 Day 05,
# which will display a specified message when solved.
# The message should be two 9-character strings.
 
from random import randrange, choice
 
generated_filename = "generated.txt"
 
#############################################################
 
 
def count_conflicts(p1, p2):
    conflicts = 0
    for s1, s2 in zip(p1, p2):
        for c1, c2 in zip(s1, s2):
            conflicts += c1 != '.' and c2 != '.' and c1 != c2
    return conflicts
 
 
def generate_stack(message):
    p1 = message[0]
    p2 = message[1]
 
    p1 = [""] + [c + "." * 9 for c in p1]
    p2 = [""] + [c + "." * 9 for c in p2]
 
    moves = []
    for i in range(500):
        src = randrange(1, 10)
        while len(p1[src]) == 0:
            src = randrange(1, 10)
        dest = randrange(1, 10)
        while dest == src:
            dest = randrange(1, 10)
        n = randrange(1, 2 + len(p1[src]) // 2)
 
        moves.append((n, src, dest))
 
        p1[src], p1[dest] = p1[src][n:], p1[src][:n][::-1] + p1[dest]
        p2[src], p2[dest] = p2[src][n:], p2[src][:n] + p2[dest]
 
    return moves, p1, p2
 
 
#############################################################
# Input the message to hide
 
message = input("Desired message (default: CHRISTMAS GREETINGS)? ")
message = message.upper().split()
if len(message) == 0:
    message = ["CHRISTMAS", "GREETINGS"]
elif len(message) == 1:
    message = [message[0], "CHRISTMAS"]
message = [part[:9].ljust(9).replace(" ", ".") for part in message[:2]]
 
#############################################################
print("Generating stack to display", message)
 
while True:
    moves, p1, p2 = generate_stack(message)
    conflicts = count_conflicts(p1, p2)
    if conflicts == 0 and min(len(s) for s in p1[1:]) > 0:
        break
 
print("Valid configuration found.")
 
#############################################################
# fill in the stacks' unallocated elements
maxlen = max(len(s) for s in p1)
stacks = []
for s1, s2 in zip(p1, p2):
    stack = ""
    for c1, c2 in zip(s1, s2):
        if c1 != '.':
            stack += c1
        elif c2 != '.':
            stack += c2
        else:
            stack += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    stacks.append(stack.rjust(maxlen))
 
#############################################################
# Output the datafile.
 
outf = open(generated_filename, "wt")
for i in range(maxlen):
    line = []
    for s in stacks[1:]:
        if s[i] == " ":
            line.append("   ")
        else:
            line.append("[" + s[i] + "]")
    print(" ".join(line), file=outf)
print(" 1   2   3   4   5   6   7   8   9 ", file=outf)
print(file=outf)
 
for n, src, dest in moves[:0:-1]:
    print("move", n, "from", dest, "to", src, file=outf)
n, src, dest = moves[0]
print("move", n, "from", dest, "to", src, end="", file=outf)
 
outf.close()
print("Data saved to", generated_filename)