# solve the 8 puzzle problem using hill climbing algorithm(steepest ascent)

# store the starting puzzle state
puzzle = []

# store the goal state:
# assuming its this for now
# 1 2 3
# 4 5 6
# 7 8 .

# assuming a 0 is the blank space
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

print("Enter the starting puzzle state:")
for i in range(3):
    tempList = []
    for j in range(3):
        i = int(input(f"Enter the {i}th row:"))
        tempList.append(i)
    puzzle.append(tempList)
    
path = []

def heuristic(currentState):
    pass


def hillClimb8Puzzle(currentState):
    
    # check if goal state reached
    # ! do something here
    if currentState == goal:
        pass
    
    # compute indices that can be swapped with the blank space:
    emptyI = 0
    emptyJ = 0
    for i in range(3):
        for j in range(3):
            if currentState[i][j] == 0:
                emptyI = i
                emptyJ = j
    # make lists for each neighbour of emptyI and emptyJ, too sleepy to do it now
            