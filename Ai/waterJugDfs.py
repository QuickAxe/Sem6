# jug 1 capacity = jug1
# jug 2 capacity = jug2

print("Enter jug 1 capacity:")

jug1 = int(input())
jug2 = int(input("Enter jug 2 capacity: "))

goal = int(input("Enter goal state: "))

goalSet = []

for i in range(jug1 + 1):
    goalSet.append((i, goal))

for j in range(jug2 + 1):
    goalSet.append((goal, j))


path = []
visited = []

# storing start state
# path.append((0, 0, "start"))

state = 0


def jugsDfs(currentState, state):

    jug1, jug2, _ = currentState

    if (jug1, jug2) in visited:
        return
    global path
    path.append(currentState)

    visited.append((jug1, jug2))

    # if goal reached:
    if (jug1, jug2) in goalSet:
        print(*path, sep="\n")
        print("reached goal state! \n")
        return

    if jug1 > 0:
        jugsDfs((0, jug2, "Emptying X"), state + 1)

    if jug2 > 0:
        jugsDfs((jug1, 0, "Emptying Y"), state + 1)

    if jug1 < 4:
        jugsDfs((4, jug2, "Filling X"), state + 1)

    if jug2 < 3:
        jugsDfs((jug1, 3, "Filling Y"), state + 1)

    if jug1 > 0 and jug2 < 3:

        if jug1 + jug2 <= 3:
            jugsDfs((0, jug1 + jug2, "Pouring from X to Y"), state + 1)

        else:
            jugsDfs((jug1 - (3 - jug2), 3, "Pouring from X to Y"), state + 1)

    if jug1 < 4 and jug2 > 0:

        if jug1 + jug2 <= 4:
            jugsDfs((jug1 + jug2, 0, "Pouring from Y to X"), state + 1)

        else:
            jugsDfs((4, jug2 - (4 - jug1), "Pouring from Y to X"), state + 1)

    path.pop(-1)


jugsDfs((0, 0, "Start"), state)
