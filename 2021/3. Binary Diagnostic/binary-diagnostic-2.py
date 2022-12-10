import os

filename = "binary-diagnostic.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    oxygenRating = f.read().splitlines()
    carbonRating = oxygenRating[:]
    STRLEN = len(oxygenRating[0])

list0, list1, count, decimalOxygen, decimalCarbon = [], [], [0, 0], 0, 0
for i in range(0, STRLEN):
    if len(oxygenRating) > 1:
        for j in range(0, len(oxygenRating)):
            if oxygenRating[j][i] == "0":
                count[0] += 1
                list0.append(oxygenRating[j])
            elif oxygenRating[j][i] == "1":
                count[1] += 1
                list1.append(oxygenRating[j])
        if count[1] >= count[0]:
            oxygenRating = list1[:]
            list0, list1, count = [], [], [0, 0]
        elif count[1] < count[0]:
            oxygenRating = list0[:]
            list0, list1, count = [], [], [0, 0]
for i in range(0, STRLEN):
    decimalOxygen += int(oxygenRating[0][i])*(2**(STRLEN-(i+1)))
for i in range(0, STRLEN):
    if len(carbonRating) > 1:
        for j in range(0, len(carbonRating)):
            if carbonRating[j][i] == "0":
                count[0] += 1
                list0.append(carbonRating[j])
            elif carbonRating[j][i] == "1":
                count[1] += 1
                list1.append(carbonRating[j])
        if count[0] > count[1]:
            carbonRating = list1[:]
            list0, list1, count = [], [], [0, 0]
        elif count[0] <= count[1]:
            carbonRating = list0[:]
            list0, list1, count = [], [], [0, 0]
for i in range(0, STRLEN):
    decimalCarbon += int(carbonRating[0][i])*(2**(STRLEN-(i+1)))
print(decimalOxygen*decimalCarbon)