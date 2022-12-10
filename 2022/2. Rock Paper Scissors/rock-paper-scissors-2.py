import os

filename = "rock-paper-scissors.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

totalscore = 0
for i in range(0, len(content)):
    temp = content[i].split(" ")
    match temp[0]:
        case "A": 
            match temp[1]:
                case "X": totalscore += 3
                case "Y": totalscore += 4
                case "Z": totalscore += 8
        case "B":
            match temp[1]:
                case "X": totalscore += 1
                case "Y": totalscore += 5
                case "Z": totalscore += 9
        case "C":
            match temp[1]:
                case "X": totalscore += 2
                case "Y": totalscore += 6
                case "Z": totalscore += 7
print("Part 2:", totalscore)