import os, hashlib

filename = "the-ideal-stocking-stuffer.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

i = 0
while True:
    if (hashlib.md5((f"{content}{i}").encode()).hexdigest())[:6] == "000000":
        break
    else:
        i += 1
print(i)