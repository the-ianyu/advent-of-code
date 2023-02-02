import os

filename = "binary-boarding.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

seats = []
for i in content:
    seats.append(int(i[:7].replace("B", "1").replace("F", "0"), 2)*8+int(i[7:].replace("R", "1").replace("L", "0"), 2))
seats.sort()
for i in range(1, len(seats)):
    if seats[i]-seats[i-1] == 2:
        print("Part 2:", seats[i]-1)
        break