import os
from string import ascii_lowercase as letters

filename = "some-assembly-required.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

for i in range(0, len(content)):
    content[i] = content[i].split(" -> ")
    content[i][0] = content[i][0].split(" ")

def BINARY(x):
    return ("0"*(16-len(f'{int(x):b}'))) + (f'{int(x):b}')

def AND(x, y):
    final = ""
    x, y = BINARY(x), BINARY(y)
    for i in range(0, len(x)):
        if x[i] == "1" and y[i] == "1":
            final += "1"
        else:
            final += "0"
    return int(final, 2)

def OR(x, y):
    final = ""
    x, y = BINARY(x), BINARY(y)
    for i in range(0, len(x)):
        if x[i] == "1" or y[i] == "1":
            final += "1"
        else:
            final += "0"
    return int(final, 2)

def NOT(x):
    final = ""
    x = BINARY(x)
    for i in range(0, len(x)):
        if x[i] == "1":
            final += "0"
        else:
            final += "1"
    return int(final, 2)

def LSHIFT(x, num):
    return x << num

def RSHIFT(x, num):
    return x >> num

lst = [["" for _ in range(26)] for _ in range(27)]

for i in range(0, len(content)):
    try:
        content[i][0][0] = int(content[i][0][0])
        if len(content[i][0]) == 1:
            print(len(content[i][1]))
            if len(content[i][1]) == 1:
                lst[0][letters.find(content[i][1])] = content[i][0][0]
                content[i][0][0] = "null"
            elif len(content[i][1]):
                lst[letters.find(content[i][1][0])][letters.find(content[i][1][1])] = content[i][0][0]
                content[i][0][0] = "null"
    except:
        pass

old_lst = []
while old_lst != lst:
    old_lst = lst[:]
    for i in range(0, len(content)):
        pass

# lett_ers = " " + letters
# old_lst = []

# print(content[1][0])
# while lst != old_lst:
#     temp_lst = lst[:]
#     for i in range(len(content)):
#         if len(content[i][1]) == 1:
#             pos = letters.find(content[i][1])
#             match content[i][0][1]:
#                 case "AND":
#                     lst[0][pos] = AND(int(content[i][0][0]), int(content[i][0][2]))
#                 case "OR":
#                     lst[0][pos] = OR(int(content[i][0][0]), int(content[i][0][2]))
#                 case "LSHIFT":
#                     lst[0][pos] = LSHIFT(int(content[i][0][0]), int(content[i][0][2]))
#                 case "RSHIFT":
#                     lst[0][pos] = RSHIFT(int(content[i][0][0]), int(content[i][0][2]))
#         elif len(content[i][1]) == 2:
#             pos1, pos2 = letters.find(content[i][1][0]), letters.find(content[i][1][1])
#             match content[i][0][1]:
#                 case "AND":
#                     lst[pos1][pos2] = AND(int(content[i][0][0]), int(content[i][0][2]))
#                 case "OR":
#                     lst[pos1][pos2] = OR(int(content[i][0][0]), int(content[i][0][2]))
#                 case "LSHIFT":
#                     lst[pos1][pos2] = LSHIFT(int(content[i][0][0]), int(content[i][0][2]))
#                 case "RSHIFT":
#                     lst[pos1][pos2] = RSHIFT(int(content[i][0][0]), int(content[i][0][2]))
#     old_lst = temp_lst[:]

# x = 123
# y = 456
# d = AND(x, y)
# e = OR(x, y)
# f = LSHIFT(x, 2)
# g = RSHIFT(y, 2)
# h = NOT(x)
# i = NOT(y)

# print(f'{x=}')
# print(f'{y=}')
# print(f'{d=}')
# print(f'{e=}')
# print(f'{f=}')
# print(f'{g=}')
# print(f'{h=}')
# print(f'{i=}')