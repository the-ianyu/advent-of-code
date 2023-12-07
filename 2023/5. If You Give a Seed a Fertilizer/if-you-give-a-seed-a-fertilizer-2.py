# from os import path
# from tqdm import tqdm

# filename = 'test.txt'
# here = path.dirname(path.abspath(__file__))
# filepath = path.join(here, filename)

# with open(filepath, 'r') as f:
#     content = f.read().splitlines()
#     temp = [int(x) for x in content[0][content[0].find(":")+2:].split()]
#     maps = [[] for _ in range(7)]
#     ptr = -1
#     flagnext = False
#     for i in content[1:]:
#         if flagnext:
#             flagnext = False
#             continue
#         if i == '':
#             ptr += 1
#             flagnext = True
#             continue
#         maps[ptr].append([int(x) for x in i.split()])

# minimum = float("inf")
# for i in tqdm(range(0, len(temp), 2)):
#     for j in tqdm(range(temp[i], temp[i]+temp[i+1])):
#         loc = j
#         for k in maps:
#             for l in k:
#                 if l[1] <= loc < l[1]+l[2]:
#                     loc += l[0]-l[1]
#                     break
#         minimum = min(loc, minimum)
# print("Part 2:", minimum)
