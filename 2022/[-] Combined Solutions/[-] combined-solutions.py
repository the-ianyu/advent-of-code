from os import path as p
from string import ascii_letters as letters
masterlist = [["BLANK"] if i == 0 else [] for i in range(26)]
# --
def opener(filename):
    here = p.dirname(p.abspath(__file__))
    filepath = p.join(here, filename)
    with open(filepath, "r") as f:
        return f.read()
class class_day1:
    def __init__(self, content):
        finalarray, temp = [], 0
        for i in range(0, len(content)):
            if content[i] != "":
                temp += int(content[i])
            else:
                finalarray.append(int(temp))
                temp = 0
        finalarray.sort()
        self.finalarray = finalarray
    def part1(self):
        return self.finalarray[-1:][0]
    def part2(self):
        return sum(self.finalarray[-3:])
class class_day2:
    def __init__(self, content):
        self.content = content
        self.p1 = [4,8,3,1,5,9,7,2,6]
        self.p2 = [3,4,8,1,5,9,2,6,7]
    def main(lst, content):
        totalscore = 0
        for i in range(0, len(content)):
            temp = content[i].split(" ")
            match temp[0]:
                case "A": 
                    match temp[1]:
                        case "X": totalscore += lst[0]
                        case "Y": totalscore += lst[1]
                        case "Z": totalscore += lst[2]
                case "B":
                    match temp[1]:
                        case "X": totalscore += lst[3]
                        case "Y": totalscore += lst[4]
                        case "Z": totalscore += lst[5]
                case "C":
                    match temp[1]:
                        case "X": totalscore += lst[6]
                        case "Y": totalscore += lst[7]
                        case "Z": totalscore += lst[8]
        return totalscore
    def part1(self):
        return class_day2.main(self.p1, self.content)
    def part2(self):
        return class_day2.main(self.p2, self.content)
class class_day3:
    def __init__(self, content):
        global letters
        self.content = content
        self.letters = letters
    def part1(self):
        total = 0
        for i in range(0, len(self.content)): 
            part1, part2 = self.content[i][:(len(self.content[i])//2)], self.content[i][(len(self.content[i])//2):] 
            for j in range(0, len(part1)): 
                if part1[j] in part2: 
                    total += (self.letters.index(part1[j]))+1 
                    break
        return total
    def part2(self):
        total = 0 
        for i in range(0, len(self.content), 3): 
            part1, part2, part3 = self.content[i], self.content[i+1], self.content[i+2] 
            for j in range(0, len(part3)): 
                if part3[j] in part1 and part3[j] in part2: 
                    total += (self.letters.index(part3[j]))+1 
                    break 
        return total
class class_day4:
    def __init__(self, content):
        self.content = content
    def part1(self):
        enclosed = 0
        for i in range(0, len(self.content)):
            tmp = [x.split("-") for x in self.content[i].split(",")]
            if int(tmp[0][0]) < int(tmp[1][0]) and int(tmp[0][1]) >= int(tmp[1][1]):
                enclosed += 1
            elif int(tmp[0][0]) > int(tmp[1][0]) and int(tmp[0][1]) <= int(tmp[1][1]):
                enclosed += 1
            elif int(tmp[0][0]) == int(tmp[1][0]):
                enclosed += 1
        return enclosed
    def part2(self):
        overlap = 0
        for i in range(0, len(self.content)):
            tmp = [x.split("-") for x in self.content[i].split(",")]
            lst0 = [int(x) for x in range(int(tmp[0][0]), int(tmp[0][1])+1)]
            lst1 = [int(x) for x in range(int(tmp[1][0]), int(tmp[1][1])+1)]
            for j in range(0, len(lst0)):
                if lst0[j] in lst1:
                    overlap += 1
                    break
        return overlap

day1 = class_day1(opener("calorie-counting.txt").splitlines())
masterlist[1].append(day1.part1())
masterlist[1].append(day1.part2())

day2 = class_day2(opener("rock-paper-scissors.txt").splitlines())
masterlist[2].append(day2.part1())
masterlist[2].append(day2.part2())

day3 = class_day3(opener("rucksack-reorganization.txt").splitlines())
masterlist[3].append(day3.part1())
masterlist[3].append(day3.part2())

day4 = class_day4(opener("camp-cleanup.txt").splitlines())
masterlist[4].append(day4.part1())
masterlist[4].append(day4.part2())

while True:
    try:
        inputlst = input("Which answer do you want? (Day, Part) >> ").split(", ")
        print(f"Day {inputlst[0]}, Part {inputlst[1]}: {masterlist[int(inputlst[0])][int(inputlst[1])-1]}")
    except:
        if "exit" in inputlst[0]:
            exit()
        print("Invalid input. Please try again.")