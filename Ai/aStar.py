# find the shortest path using the A* algorithm

heuristic = {
    "S": 14,
    "D": 12,
    "F": 12,
    "A": 11,
    "L": 10,
    "I": 10,
    "J": 8,
    "H": 8,
    "B": 10,
    "C": 8,
    "K": 6,
    "N": 4,
    "P": 5,
    "O": 8,
    "R": 6,
    "E": 5,
    "T": 3,
    "Q": 1,
    "G": 0,
}

graph = {
    "S": [("D", 25)],
    "D": [("F", 24), ("A", 32), ("S", 25), ("I", 26)],
    "F": [("L", 27), ("D", 24)],
    "A": [("D", 32), ("B", 11), ("H", 36)],
    "L": [("F", 27), ("I", 21), ("O", 26), ("M", 32)],
    "B": [("A", 11), ("K", 42), ("C", 24)],
    "I": [("D", 26), ("L", 21), ("J", 22)],
    "M": [("L", 32), ("P", 23), ("J", 20)],
    "P": [("M", 23)],
    "J": [("H", 22), ("I", 22), ("M", 20)],
    "H": [("A", 36), ("J", 22), ("N", 44), ("K", 28)],
    "C": [("B", 24), ("E", 40)],
    "E": [("C", 40), ("K", 32)],
    "K": [("E", 32), ("B", 42), ("H", 28), ("N", 27), ("Q", 62)],
    "N": [("K", 27), ("H", 44), ("Q", 32), ("G", 42)],
    "O": [("L", 26), ("R", 27)],
    "R": [("O", 27), ("T", 52)],
    "T": [("R", 52), ("G", 32)],
    "G": [("T", 32), ("N", 42)],
    "Q": [("N", 32), ("K", 62)],
}

open = []
closed = []

# store tuples in the format (node, parent, (g+h value))
open.append(("S", None, heuristic["S"]))

while len(open) != 0:

    # Find the min node in the open list
    minNode = min(open, key=lambda tup: tup[2])
    minNodeIndex = open.index(minNode)
    node, parent, parentFvalue = open.pop(minNodeIndex)
    
    # add to closed now
    closed.append((node, parent))

    # find the children of the node, and add to open
    for children in graph[node]:

        child, distance = children

        if child in [x[0] for x in closed]:
            continue

        childFvalue = distance + heuristic[child] + parentFvalue

        # check open list if this child already exists, and if this new path is shorter, update it
        for i, nodes in enumerate(open):
            oldPathChild, _, oldFvalue = nodes

            # update path
            if oldPathChild == child and oldFvalue > childFvalue:
                # remove the old tuple
                open.pop(i)

        open.append((child, node, childFvalue))

path = []

