# code to play tic tac toe against a player, using the minimax algorithm
# the player is the maximising player here, playing with 'X',
# while the AI is the minimising player playing with 'O'

from copy import deepcopy


# function to check if a player has won, and return the respective heuristic value
def heuristic(state):
    """
    returns if a player has won
    ### Arguments:
    state: the state to check the heuristic for
    """

    # check each row
    for row in range(3):
        if state[row][0] == state[row][1] and state[row][1] == state[row][2]:
            if state[row][0] == "X":
                return 100
            elif state[row] == "O":
                return -100

    # now check for each column
    for column in range(3):
        if (
            state[0][column] == state[1][column]
            and state[1][column] == state[2][column]
        ):
            if state[0][column] == "X":
                return 100
            elif state[0][column] == "O":
                return -100

    # now check for diagonals:
    if (state[0][0] == state[1][1] and state[1][1] == state[2][2]) or (
        state[0][2] == state[1][1] and state[1][1] == state[2][0]
    ):
        if state[1][1] == "X":
            return 100
        elif state[1][1] == "O":
            return -100

    # if it is a draw, or any other state:
    return 0


def genChildren(state, maxPlayer):

    children = []

    for i in range(3):
        for j in range(3):
            tempState = deepcopy(state)
            if tempState[i][j] == "_":
                if maxPlayer:
                    tempState[i][j] = "X"
                else:
                    tempState[i][j] = "O"
                temptempState = deepcopy(tempState)
                children.append(temptempState)
                tempState[i][j] = "_"

    return children


def minimax(state, maxPlayer):

    heuristicValue = heuristic(state)

    # if the player has won, return the heuristic value
    if abs(heuristicValue) == 100:
        return heuristicValue

    children = []
    heuristics = []

    if maxPlayer:
        # find the best move to make here:
        children = genChildren(state, maxPlayer)

        # if its a leaf node, and has no further children
        if len(children) == 0:
            return heuristic(state)

        # find the heuristic value of each child
        for child in children:
            heuristicValue = minimax(child, False)
            heuristics.append(heuristicValue)

        # find max heuristic:
        max = -99999
        for i in range(len(children)):
            if heuristics[i] > max:
                max = heuristics[i]

        return max
    else:
        # find the best move to make here:
        children = genChildren(state, maxPlayer)

        # if its a leaf node, and has no further children
        if len(children) == 0:
            return heuristic(state)

        # find the heuristic value of each child
        for child in children:
            heuristicValue = minimax(child, True)
            heuristics.append(heuristicValue)

        # find min heuristic:
        min = 99999
        for i in range(len(children)):
            if heuristics[i] < min:
                min = heuristics[i]

        return min


def movesLeft(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == "_":
                return True


def playGame():

    print("You will play as 'X', against the AI. Good luck.....\n")

    # store the board state
    state = [["_" for i in range(3)] for j in range(3)]

    print(*state, sep="\n")

    global drawFlag

    while movesLeft(state):

        print("enter the matrix coordinates of where you want to play:")
        x, y = input().split()
        x = int(x)
        y = int(y)

        # check if the move is valid or not
        if x not in range(3) and y not in range(3):
            print("Invalid coordinates, enter again")
            print()
            continue

        if state[x][y] != "_":
            print("Oi, no cheating, you cant overrite a move.... enter again")
            print()
            continue

        state[x][y] = "X"

        print("your move: ")
        print(*state, sep="\n")

        # check if player won:
        if heuristic(state) == 100:
            print("YAYY, you won and beat the ai...")
            print("exiting game....")
            drawFlag = False
            return

        # choose best move for ai
        moves = []
        heuristics = []

        moves = genChildren(state, False)

        for move in moves:
            heuristics.append(minimax(move, True))

        # choose the best move
        min = 99999
        for i in range(len(moves)):
            if heuristics[i] < min:
                min = heuristics[i]
                state = moves[i]

        print("ai move: ")
        print(*state, sep="\n")

        # check if the ai won
        if heuristic(state) == -100:
            print("Oh no, the ai beat you...")
            print("exiting game....")
            drawFlag = False
            return


drawFlag = True

if __name__ == "__main__":
    playGame()

    if drawFlag:
        print("Oh! its a draw...")
        print()
