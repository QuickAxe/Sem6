#  state -> (missionaries, cannibals, boat) on right bank
#  goal -> (0, 0, R)

print("Enter number of missionaries :")

missionaries = int(input())
cannibals = int(input("Enter no of cannibals: "))


path = []
visited = []

solution = 0


def missionariesCannibalsDfs(currentState):

    currentMissonaries, currentCannibals, boat = currentState

    # check if state is illegal
    # if (
    #     (currentMissonaries < currentCannibals)
    #     or ((missionaries - currentMissonaries) < (cannibals - currentCannibals))
    # ) and (currentMissonaries != 0 or currentMissonaries != missionaries):
    #     return

    if not (
        (currentMissonaries == currentCannibals)
        or (currentMissonaries in [0, missionaries])
    ):
        return

    global visited

    # check if current state has been visited previously
    if (currentMissonaries, currentCannibals, boat) in visited:
        return

    global path
    path.append(currentState)

    # check if goal state reached
    if currentState == (0, 0, "R"):
        print(*path, sep=", ")
        print("reached goal state! \n")
        global solution
        solution += 1
        return

    visited.append((currentMissonaries, currentCannibals, boat))

    if boat == "L":
        if currentMissonaries > 0 and currentCannibals > 0:
            missionariesCannibalsDfs(
                (currentMissonaries - 1, currentCannibals - 1, "R")
            )

        if currentMissonaries > 0:
            missionariesCannibalsDfs((currentMissonaries - 1, currentCannibals, "R"))

        if currentCannibals > 0:
            missionariesCannibalsDfs((currentMissonaries, currentCannibals - 1, "R"))

        if currentCannibals > cannibals - 2:
            missionariesCannibalsDfs((currentMissonaries, currentCannibals - 2, "R"))

        if currentMissonaries > missionaries - 2:
            missionariesCannibalsDfs((currentMissonaries - 2, currentCannibals, "R"))

    elif boat == "R":
        if currentMissonaries < missionaries and currentCannibals < cannibals:
            missionariesCannibalsDfs(
                (currentMissonaries + 1, currentCannibals + 1, "L")
            )

        if currentMissonaries < missionaries:
            missionariesCannibalsDfs((currentMissonaries + 1, currentCannibals, "L"))

        if currentCannibals < cannibals:
            missionariesCannibalsDfs((currentMissonaries, currentCannibals + 1, "L"))

        if currentCannibals < cannibals - 1:
            missionariesCannibalsDfs((currentMissonaries, currentCannibals + 2, "L"))

        if currentMissonaries < missionaries - 1:
            missionariesCannibalsDfs((currentMissonaries + 2, currentCannibals, "L"))

    path.pop(-1)


missionariesCannibalsDfs((missionaries, cannibals, "L"))

if solution == 0:
    print("No solution\n")
