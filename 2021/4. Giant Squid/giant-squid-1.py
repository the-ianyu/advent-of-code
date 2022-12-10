import os

filename = "giant-squid.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = (f.read().splitlines())
    for i in range(0, len(content)):
        content[i] = content[i].replace("  ", " 0")
        if content[i] == "":
            content[i] = content[i].replace("", " ")
        if content[i][0] == " ":
            content[i] = content[i].replace(" ", "0", 1)
        if content[i] == "0":
            content[i] = content[i].replace("0", "||")
    masterlist = [[] for _ in range(content.count("||"))]
    nos = [[0 for _ in range(10)] for _ in range(content.count("||"))]
    drawnNumbers = content[0].split(",")
    content = content[2:]
    for i in range(0, len(masterlist)):
        masterlist[i] = content[0:5]
        content = content[6:]
    del content, f, filepath, filename, here, i, os

#active = 1
#while active == 1:
#    for i in range(0, len(drawnNumbers)):
#        for j in range(0, len(masterlist)):
#           for k in range(0, 5):
#               for l in range(0, 15, 3):
#                    if masterlist[j][k][l:l+2] == drawnNumbers[i]:
#                        nos[j][k] += 1
#                        nos[j][l//3 + 5] += 1  
#        if not j <= 4:
#            for k in range(0, len(nos)):
#                for l in range(0, 10):
#                    if nos[k][l] == 1:
#                        active == 0
#print(nos)