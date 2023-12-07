from os import path

filename = "camel-cards.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, 'r') as f:
    content = [x.split() for x in f.read().splitlines()]

ranker = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q" : 11,
    "K" : 12,
    "A" : 13
}

def sorter(hand):
    counter_dict = {}
    for x in hand:
        if x in counter_dict:
            counter_dict[x] += 1
        else:
            counter_dict[x] = 1
    fh = 0
    db = 0
    for count in counter_dict.values():
        if count == 5:
            return [7] + [ranker[x] for x in hand]
        if count == 4:
            return [6] + [ranker[x] for x in hand]
        if count == 3:
            fh += 1
        if count == 2:
            db += 1
    if fh == 1 and db == 1:
        return [5] + [ranker[x] for x in hand]
    if fh == 1:
        return [4] + [ranker[x] for x in hand]
    if db == 2:
        return [3] + [ranker[x] for x in hand]
    if db == 1:
        return [2] + [ranker[x] for x in hand]
    if all(x == 1 for x in counter_dict.values()):
        return [1] + [ranker[x] for x in hand]

content.sort(key=lambda x: sorter(x[0]))
print("Part 1:", sum((i+1)*int(content[i][1]) for i in range(len(content))))
