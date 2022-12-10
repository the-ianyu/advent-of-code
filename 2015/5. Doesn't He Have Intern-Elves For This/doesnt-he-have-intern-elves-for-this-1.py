import os

filename = "doesnt-he-have-intern-elves-for-this.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

vowels, prohib = ["a", "e", "i", "o", "u"], ["ab", "cd", "pq", "xy"]
nice = 0
for i in range(0, len(content)):
    vowelCount, repCount = 0, 0
    for position, vowel in enumerate(content[i]):
        if vowel in vowels:
            vowelCount += 1
    for j in range(1, len(content[i])):
        if content[i][j-1] == content[i][j]:
            repCount += 1
    if any(x in content[i] for x in prohib):
        continue
    if vowelCount >= 3 and repCount >= 1:
        nice += 1
print(nice)