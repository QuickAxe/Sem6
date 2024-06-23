#  state -> (missionaries, cannibals, boat) on right bank
#  goal -> (0, 0, R)

import sys

print("Enter number of missionaries :")

missionaries = int(input())
cannibals = int(input("Enter no of cannibals: "))


parent = {}
visited = []

# list to store all penultimate goal states:
preGoalStates = set()

solution = 0

start = (missionaries, cannibals, "L")
goal = (0, 0, "R")
parent[start] = None

queue = []

queue.append(start)


def addState(nextState, parentState):
    global queue

    if nextState == goal:
        global preGoalStates
        preGoalStates.add(parentState)
        parent[nextState] = preGoalStates
    elif nextState not in visited:
        visited.append(parentState)
        parent[nextState] = currentState
    queue.append(nextState)


while len(queue) != 0:
    currentState = queue.pop(0)

    currentMissonaries, currentCannibals, boat = currentState

    # credits to this elegant condition for a valid state go to : https://github.com/SorcierMaheP
    if not (
        (currentMissonaries == currentCannibals)
        or (currentMissonaries in [0, missionaries])
    ):
        continue

    # check if goal state reached
    if currentState == goal:

        # get the list of parents of the goal state
        parents = parent[currentState]

        for par in parents:

            path = []
            path.append(currentState)
            solution += 1
            tempState = par
            while tempState in parent and parent[tempState] is not None:
                path.append(tempState)
                tempState = parent[tempState]

            path.append(start)
            path.reverse()
            print(*path, sep=", ")
            print("reached goal state! \n")

        sys.exit()

    else:

        # check for each rule, and add to queue accordingly
        if boat == "L":
            if currentMissonaries > 0 and currentCannibals > 0:
                nextState = (currentMissonaries - 1, currentCannibals - 1, "R")
                addState(nextState, currentState)
            if currentMissonaries > 0:
                nextState = (currentMissonaries - 1, currentCannibals, "R")
                addState(nextState, currentState)
            if currentCannibals > 0:
                nextState = (currentMissonaries, currentCannibals - 1, "R")
                addState(nextState, currentState)
            if currentCannibals > cannibals - 2:
                nextState = (currentMissonaries, currentCannibals - 2, "R")
                addState(nextState, currentState)
            if currentMissonaries > missionaries - 2:
                nextState = (currentMissonaries - 2, currentCannibals, "R")
                addState(nextState, currentState)
        elif boat == "R":
            if currentMissonaries < missionaries and currentCannibals < cannibals:
                nextState = (currentMissonaries + 1, currentCannibals + 1, "L")
                addState(nextState, currentState)
            if currentMissonaries < missionaries:
                nextState = (currentMissonaries + 1, currentCannibals, "L")
                addState(nextState, currentState)
            if currentCannibals < cannibals:
                nextState = (currentMissonaries, currentCannibals + 1, "L")
                addState(nextState, currentState)
            if currentCannibals < cannibals - 1:
                nextState = (currentMissonaries, currentCannibals + 2, "L")
                addState(nextState, currentState)
            if currentMissonaries < missionaries - 1:
                nextState = (currentMissonaries + 2, currentCannibals, "L")
                addState(nextState, currentState)
if solution == 0:
    print("No solution, :(")
