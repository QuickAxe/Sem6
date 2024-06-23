# perform best first search in state space to solve the n queens problem

import random
from copy import copy


n = int(input("Enter the value of n: "))

# store the state as a list of the positions of the queens, per row
state = [random.randint(0, n-1) for i in range(n)]

# store all the visited states:
visited = []

# flag if there is no solution
noGoalFlag = True

# # store some valid state
# state = [[1 if i==j else 0 for i in range(n)] for j in range(n)]

# # function to find the heuristic for each state
# def heuristic(state):

#     heuristicValue = 0
#     locations = []
#     # count the number of conflicting queens along rows and columns
#     for i in range(n):
#         rowSum = -1
#         columnSum = -1
#         for j in range(n):
#             if state[i][j]:
#                 locations.append((i, j))
#             rowSum += state[i][j]
#             columnSum += state[j][i]

#         if rowSum > 0:
#             heuristicValue += rowSum
#         if columnSum > 0:
#             heuristicValue += columnSum

#     # count the number of conflicting queens along diagonals
#     for key_i, loc in enumerate(locations):
#         for loc2 in locations[key_i:]:
#             # loc loc2 are two tuples
#             # (i, j)
#             #   (0,0)
#             #   Q _ _
#             #   _ _ _
#             #   _ _ Q (2,2)
#             # if the difference between the xs and the ys is the same, it
#             # must be on a diagonal (hopefully)

#             if abs(loc[0] - loc2[0]) == abs(loc[1] - loc2[1]):
#                 heuristicValue += 1

#     return heuristicValue

#  state[i]= [0, 1, 0, 3]
#       i = 0 1 2 3
#           1 0 1 0
#           0 1 0 0
#           0 0 0 1

# ================================================ Utility Functions ====================================


# this function was partially contributed by : https://github.com/TheInvincible95
def heuristic(state):

    # store the (x, y) coordinates of the queens
    locations = list(enumerate(state))
    heuristicValue = 0

    for key_i, loc in enumerate(locations):
        for loc2 in locations[key_i + 1:]:
            # loc loc2 are two tuples
            # (i, j)
            #   (0,0)
            #   Q _ _
            #   _ _ _
            #   _ _ Q (2,2)

            # if the two queens are in the same column
            if loc[1] == loc2[1]:
                heuristicValue += 1

            # if the difference between the x and the y coordinates
            # of both queens is the same, ie |(x2 - x1)| == |(y2 - y1)|
            # it must be on a diagonal (hopefully)
            if abs(loc[0] - loc2[0]) == abs(loc[1] - loc2[1]):
                heuristicValue += 1

    return heuristicValue


# generate all possible children of the state given
def genChildren(state):
    """
    generate all possible children of the state given
    ### Args:
    state: a list of positions of each queen, per row
    """
    children = []

    # loop to generate different children by changing each row at a time
    for i in range(n):

        child = copy(state)

        # place queens in the i'th row in all other positions other than the current one
        for j in range(n):
            if j != state[i]:
                child[i] = j
                if child not in visited:
                    children.append(copy(child))
                    # add it to visited
                    visited.append(copy(child))

    return children


def printBoard(state):

    for row in state:
        for column in range(n):
            if column == row:
                print("Q", sep=" ", end=" ")
            else:
                print("x", sep=" ", end=" ")
        print()


# ========================================================================================================


def bestFirstNQueens(start):

    # store the children of the current state
    children = []
    # a queue to store tuples of (heuristic, state) for all states in open list
    queue = []

    queue.append((heuristic(start), start))

    while len(queue) != 0:

        # get the best child from the queue
        currentHeuristic, currentState = queue.pop(0)

        print()
        printBoard(currentState)

        # check if a goal state has been reached
        if currentHeuristic == 0:
            print("goal reached")
            printBoard(currentState)
            global noGoalFlag
            noGoalFlag = False
            return
        # add it to visited
        visited.append(copy(currentState))

        # generate all children of the current state, that have not already been visited:
        children = genChildren(currentState)

        # compute the heuristic of each child, and add it to the queue:
        for child in children:
            queue.append((heuristic(child), copy(child)))

        # sort the queue based on heuristic values:
        queue.sort()


bestFirstNQueens(state)

if noGoalFlag:
    print("No solution :(")
