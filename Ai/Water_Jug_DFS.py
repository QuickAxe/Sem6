import sys

START = (0, 0, "Start")
Visited = []
Visited.append(START[:2])
Parent = {}
Parent[START] = None


def DFSAdd(tuple, tup, GOAL_SET):
    if tup[:2] not in Visited:
        Parent[tup] = tuple
        Visited.append(tup[:2])
        Rules(tup, GOAL_SET)


def Rules(tuple, GOAL_SET):
    jug1, jug2,_ = tuple
    if tuple[:2] in GOAL_SET:
        path = []
        while tuple in Parent and Parent[tuple] is not None:
            path.append(tuple)
            tuple = Parent[tuple]
        path.append(START)
        path.reverse()
        print(*path, sep="\n")
        sys.exit()
    if jug1 < 4:
        tup = (4, jug2, "Filled 4g")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug2 < 3:
        tup = (jug1, 3, "Filled 3g")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug1 > 0:
        tup = (0, jug2, "Emptied 4g")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug2 > 0:
        tup = (jug1, 0, "Emptied 3g")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug1 + jug2 < 7 and 4 - jug1 < jug2:
        tup = (4, jug2 - (4 - jug1), "Transferred 3g to 4g with some remaining")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug1 + jug2 < 7 and 3 - jug2 < jug1:
        tup = (jug1 - (3 - jug2), 3, "Transferred 4g to 3g with some remaining")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug1 + jug2 < 4:
        tup = (jug1 + jug2, 0, "Entirely transferred 3g to 4g")
        DFSAdd(tuple, tup, GOAL_SET)
    if jug1 + jug2 < 3:
        tup = (0, jug1 + jug2, "Entirely transferred 4g to 3g")
        DFSAdd(tuple, tup, GOAL_SET)


jug = int(input("Enter 0 for 4g jug, 1 for 3g jug"))
cap = int(input("Enter the capacity for the goal state"))
GOAL_SET = []
if not jug:
    for i in range(4):
        GOAL_SET.append((cap, i))
else:
    for i in range(5):
        GOAL_SET.append((i, cap))
Rules(START, GOAL_SET)
