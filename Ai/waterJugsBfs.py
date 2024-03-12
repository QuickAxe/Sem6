from collections import deque

def jugBfs(start, target, leftCapacity, rightCapacity):
    q = deque()
    q.append((start, [(0, 0)]))
    visited = set()

    while q:
        currState, path = q.popleft()
        left, right = currState

        if left == target or right == target:
            allPaths.append(path)
            continue

        visited.add(currState)
        possibleStates = [(leftCapacity, right), (left, rightCapacity), (0, right), (left, 0)]

        # Pouring from right jug to left jug
        pourLeft = leftCapacity - left
        if pourLeft >= right:
            possibleStates.append((left + right, 0))
        else:
            possibleStates.append((leftCapacity, right - pourLeft))

        # Pouring from left jug to right jug
        pourRight = rightCapacity - right
        if pourRight >= left:
            possibleStates.append((0, left + right))
        else:
            possibleStates.append((left - pourRight, rightCapacity))

        for state in possibleStates:
            if state not in visited:
                q.append((state, path + [state]))

allPaths = []
targetCapacity = int(input('Enter the target capacity: '))
leftJugCapacity = int(input('Enter the capacity of the left jug: '))
rightJugCapacity = int(input('Enter the capacity of the right jug: '))

jugBfs((0, 0), targetCapacity, leftJugCapacity, rightJugCapacity)

if len(allPaths) == 0:
    print('No solution')
else:
    for path in allPaths:
        print(path)