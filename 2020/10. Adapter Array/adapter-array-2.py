# import os, functools

# filename = "adapter-array.txt"
# here = os.path.dirname(os.path.abspath(__file__))
# filepath = os.path.join(here, filename)

# with open(filepath, "r") as f:
#     content = sorted([int(x) for x in f.read().splitlines()])
# content = [0] + content + [content[-1]+3]
# content = tuple(content)
# print(content)
# # content = (0, 1, 4, 6, 7, 9, 12) #testcase

# def getNeighbors(node):
#     global content
#     neighbours = []
#     for i in range(1, 4):
#         if node+i in content:
#             neighbours.append(node+i)
#     return tuple(neighbours)
# @functools.lru_cache(maxsize=None)
# def nodesearch(node):
#     global content
#     total = 0
#     neighbors = getNeighbors(node)
#     total += len(neighbors)
#     for x in neighbors:
#         total += nodesearch(x)
#     return total

# print(nodesearch(0))