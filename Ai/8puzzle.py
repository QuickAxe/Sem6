# solve the 8 puzzle problem using hill climbing algorithm(steepest ascent)

from copy import deepcopy

# store the starting puzzle state
# puzzle = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
puzzle = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]


# assuming a 0 is the blank space
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# goal = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]


def heuristic(currentState):
    heuristicValue = 0
    for i in range(3):
        for j in range(3):
            goalI, goalJ = findIndex(goal, currentState[i][j])

            # find manhattan distance:
            heuristicValue += abs(goalI - i) + abs(goalJ - j)

    return heuristicValue


def findIndex(matrix, value):
    tempI = 0
    tempJ = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == value:
                tempI = i
                tempJ = j
                break

    return (tempI, tempJ)


def hillClimb8Puzzle(currentState):

    # check if goal state reached
    if currentState == goal:
        print("reached goal!!")
        return

    print(currentState)

    # compute indices that can be swapped with the blank space:
    emptyI, emptyJ = findIndex(puzzle, 0)

    # ================= make a list for each neighbour of emptyI and emptyJ =========
    neighbours = []

    if (emptyI - 1) > 0:
        neighbours.append([emptyI - 1, emptyJ])
    if emptyJ - 1 > 0:
        neighbours.append([emptyI, emptyJ - 1])
    if (emptyI + 1) < 3:
        neighbours.append([emptyI + 1, emptyJ])
    if emptyJ + 1 < 3:
        neighbours.append([emptyI, emptyJ + 1])

    # ================================ generate children ============================
    children = []

    for i in range(len(neighbours)):
        swapI, swapJ = neighbours[i]
        child = deepcopy(currentState)

        temp = child[swapI][swapJ]
        child[swapI][swapJ] = child[emptyI][emptyJ]
        child[emptyI][emptyJ] = temp

        children.append(child)

    # =============================== compute highest heuristic among all children ===============

    largest = 9999999999
    largestIndex = 0
    for i, child in enumerate(children):
        if largest > (val := heuristic(child)):
            largest = val
            largestIndex = i

    # find if best child has heuristic value greather than parent, only then visit it
    parentHeuristic = heuristic(currentState)

    if largest < parentHeuristic:
        hillClimb8Puzzle(children[largestIndex])
    else:
        print("Cannot climb anymore, tired :(")
        print("Here's the last state:")
        print(currentState)


hillClimb8Puzzle(puzzle)
