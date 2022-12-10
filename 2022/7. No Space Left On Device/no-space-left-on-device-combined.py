import os

filename = "current.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()[1:]

current_directory = "main"
directory_list = ["main"]
directory_volume = [0]

for i in range(0, len(content)):
    if content[i][:4] == "$ cd":
        if content[i][5:] == "..":
            current_directory = current_directory[:current_directory.rfind("/")]
        else:
            current_directory = current_directory + "/" + content[i][5:]
    elif content[i][:4] == "$ ls":
        pass
    elif content[i][:3] == "dir":
        directory_list.append(current_directory + "/" + content[i][4:])
        directory_volume.append(0)    
    else:
        directory_volume[directory_list.index(current_directory)] += int(content[i][:content[i].find(" ")])

maxima, totalList = 0, []
for i in range(0, len(directory_list)):
    currento_maxima = 0
    for j in range(0, len(directory_list)):
        if directory_list[i] in directory_list[j]:
            currento_maxima += directory_volume[j]
    if currento_maxima < 100000:
        maxima += currento_maxima
    totalList.append(currento_maxima)
print("Part 1:", maxima)

deletion_requirement = sum(directory_volume) - (70000000-30000000)
totalList.sort()
for i in range(0, len(totalList)):
    if totalList[i] > deletion_requirement:
        print("Part 2:", totalList[i])
        break