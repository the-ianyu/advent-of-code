import os, string

filename = "passport-processing.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().split("\n\n")

total = 0
for i in range(0, len(content)):
    if all(x in content[i] for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        temp = [x.split(":") for x in content[i].split()]
        for x in temp:
            match x:
                case ["byr", y]:
                    if not (1920 <= int(y) <= 2002):
                        break
                case ["iyr", y]:
                    if not (2010 <= int(y) <= 2020):
                        break
                case ["eyr", y]:
                    if not (2020 <= int(y) <= 2030):
                        break
                case ["hgt", y]:
                    if (y[-2:] == "cm" and not (150 <= int(y[:-2]) <= 193)):
                        break
                    elif (y[-2:] == "in" and not (59 <= int(y[:-2]) <= 76)):
                        break
                    elif (y[-2:] not in ["cm", "in"]):
                        break
                case ["hcl", y]:
                    if y[0] != "#" or len(y) != 7 or not all(z in string.hexdigits for z in y[1:]):
                        break
                case ["ecl", y]:
                    if y not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        break
                case ["pid", y]:
                    if len(y) != 9 or not all(z in string.digits for z in y):
                        break
                case ["cid", y]:
                    pass
        else:
            total += 1
print("Part 2:", total)