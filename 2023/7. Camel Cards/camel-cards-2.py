from os import path

filename = "camel-cards.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

ranker = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q" : 11,
    "K" : 12,
    "A" : 13
}

def sorter(jokered, original):
    counter_dict = {}
    for x in jokered:
        if x in counter_dict:
            counter_dict[x] += 1
        else:
            counter_dict[x] = 1
    fh = 0
    db = 0
    for count in counter_dict.values():
        if count == 5:
            return [7] + [ranker[x] for x in original]
        if count == 4:
            return [6] + [ranker[x] for x in original]
        if count == 3:
            fh += 1
        if count == 2:
            db += 1
    if fh == 1 and db == 1:
        return [5] + [ranker[x] for x in original]
    if fh == 1:
        return [4] + [ranker[x] for x in original]
    if db == 2:
        return [3] + [ranker[x] for x in original]
    if db == 1:
        return [2] + [ranker[x] for x in original]
    if all(x == 1 for x in counter_dict.values()):
        return [1] + [ranker[x] for x in original]

content.sort(key=lambda x: max(sorter(x[0].replace("J", i), x[0]) for i in ranker.keys()))
print("Part 2:", sum((i+1)*int(content[i][1]) for i in range(len(content))))
