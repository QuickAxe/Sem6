#  state -> (missionaries, cannibals, boat) on right bank
#  goal -> (0, 0, R)

print("Enter number of missionaries :")

missionaries = int(input())
cannibals = int(input("Enter no of cannibals: "))


parent = {}
visited = []

solution = 0

start = (missionaries, cannibals, "L")
parent[start] = None

queue = []

queue.append(start)

while len(queue) != 0:
    currentState = queue.pop(0)

    currentMissonaries, currentCannibals, boat = currentState

    if not (
        (currentMissonaries == currentCannibals)
        or (currentMissonaries in [0, missionaries])
    ):
        continue

    # check if goal state reached
    if currentState == (0, 0, "R"):
        path = []

        solution += 1
        tempState = currentState

        while tempState in parent and parent[tempState] is not None:
            path.append(tempState)
            tempState = parent[tempState]

        path.append(start)
        path.reverse()
        print(*path, sep="\n")
        print("reached goal state! \n")

    else:

        visited.append((currentMissonaries, currentCannibals, boat))

        # check for each rule, and add to queue accordingly
        if boat == "L":
            if currentMissonaries > 0 and currentCannibals > 0:
                nextState = (currentMissonaries - 1, currentCannibals - 1, "R")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentMissonaries > 0:
                nextState = (currentMissonaries - 1, currentCannibals, "R")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentCannibals > 0:
                nextState = (currentMissonaries, currentCannibals - 1, "R")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentCannibals > cannibals - 2:
                nextState = (currentMissonaries, currentCannibals - 2, "R")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentMissonaries > missionaries - 2:
                nextState = (currentMissonaries - 2, currentCannibals, "R")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

        elif boat == "R":
            if currentMissonaries < missionaries and currentCannibals < cannibals:
                nextState = (currentMissonaries + 1, currentCannibals + 1, "L")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentMissonaries < missionaries:
                nextState = (currentMissonaries + 1, currentCannibals, "L")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentCannibals < cannibals:
                nextState = (currentMissonaries, currentCannibals + 1, "L")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentCannibals < cannibals - 1:
                nextState = (currentMissonaries, currentCannibals + 2, "L")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

            if currentMissonaries < missionaries - 1:
                nextState = (currentMissonaries + 2, currentCannibals, "L")
                if nextState not in visited:
                    queue.append(nextState)
                    parent[nextState] = currentState

if solution == 0:
    print("No solution, :(")
