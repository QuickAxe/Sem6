# solve the 8 puzzle problem using hill climbing algorithm(steepest ascent)

from copy import deepcopy

# store the starting puzzle state
# puzzle = [[7, 2, 4],
#           [5, 0, 6],
#           [8, 3, 1]]
puzzle = [[1, 2, 3],
          [8, 6, 0],
          [7, 5, 4]]


# assuming a 0 is the blank space
goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]
# goal = [[0, 2, 4],
#         [7, 5, 6],
#         [8, 3, 1]]


def heuristic(state):
    heuristicValue = 0
    for i in range(3):
        for j in range(3):
            goalI, goalJ = findIndex(goal, state[i][j])

            # find manhattan distance:
            if state[i][j] != 0:
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


def bestFirstSearch8Puzzle(startState):

    queue = []
    visited = []

    queue.append((heuristic(startState), startState))

    while len(queue) != 0:

        heuristicValue, state = queue.pop(0)
        visited.append(state)

        # check if goal state reached
        if state == goal:
            print("reached goal!!")
            return

        print(*state, sep="\n")
        print()

        # compute indices that can be swapped with the blank space:
        emptyI, emptyJ = findIndex(state, 0)

        # ================= make a list for each neighbour of emptyI and emptyJ =========
        neighbours = []

        if (emptyI - 1) >= 0:
            neighbours.append([emptyI - 1, emptyJ])
        if emptyJ - 1 >= 0:
            neighbours.append([emptyI, emptyJ - 1])
        if (emptyI + 1) < 3:
            neighbours.append([emptyI + 1, emptyJ])
        if emptyJ + 1 < 3:
            neighbours.append([emptyI, emptyJ + 1])

        # ================================ generate children ============================
        children = []

        for i in range(len(neighbours)):
            swapI, swapJ = neighbours[i]
            child = deepcopy(state)

            temp = child[swapI][swapJ]
            child[swapI][swapJ] = child[emptyI][emptyJ]
            child[emptyI][emptyJ] = temp

            children.append(child)

        for child in children:
            if child not in visited:
                queue.append((heuristic(child), child))

        queue.sort()


bestFirstSearch8Puzzle(puzzle)
