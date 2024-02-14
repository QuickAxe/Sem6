# jug 1 capacity = x
# jug 2 capacity = y

path = []
visited = []
goalSet = []

# storing start state
path[0] = (0, 0, "start")


#! not done
def jugsDfs(currentState):
    jug1, jug2, _ = currentState

    if tuple[:2] in goalSet:
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
        DFSAdd(tuple, tup, goalSet)
    if jug2 < 3:
        tup = (jug1, 3, "Filled 3g")
        DFSAdd(tuple, tup, goalSet)
    if jug1 > 0:
        tup = (0, jug2, "Emptied 4g")
        DFSAdd(tuple, tup, goalSet)
    if jug2 > 0:
        tup = (jug1, 0, "Emptied 3g")
        DFSAdd(tuple, tup, goalSet)
    if jug1 + jug2 < 7 and 4 - jug1 < jug2:
        tup = (4, jug2 - (4 - jug1), "Transferred 3g to 4g with some remaining")
        DFSAdd(tuple, tup, goalSet)
    if jug1 + jug2 < 7 and 3 - jug2 < jug1:
        tup = (jug1 - (3 - jug2), 3, "Transferred 4g to 3g with some remaining")
        DFSAdd(tuple, tup, goalSet)
    if jug1 + jug2 < 4:
        tup = (jug1 + jug2, 0, "Entirely transferred 3g to 4g")
        DFSAdd(tuple, tup, goalSet)
    if jug1 + jug2 < 3:
        tup = (0, jug1 + jug2, "Entirely transferred 4g to 3g")
        DFSAdd(tuple, tup, goalSet)
