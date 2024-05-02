# code to play tic tac toe against a player, using the minimax algorithm
# the player is the maximising player here, playing with 'X'

# store the board state
state = [['_' for i in range(3)] for j in range(3)]


# function to check if a player has won, and return the respective heuristic value
def heuristic(state, player):
    """
    returns if a player has won
    ### Arguments:
    player: the player making this move (x or o)
    """

    # check each row
    for row in range(3):
        if (state[row][0] == state[row][1] and state[row][1] == state[row][2]):
            if (state[row][0] == 'X'):
                return 100
            else:
                return -100

    # now check for each column
    for column in range(3):
        if (state[0][column] == state[1][column] and state[1][column] == state[2][column]):
            if (state[0][column] == 'X'):
                return 100
            else:
                return -100

    # now check for diagonals:
    if (state[0][0] == state[1][1] and state[1][1] == state[2][2]) or (state[0][2] == state[2][2] and state[2][2] == state[2][0]):
        if (state[2][2] == 'X'):
            return 100
        else:
            return -100

    # if it is a draw, or any other state:
    return 0


def minimax(state, maxPlayer):

    heuristicValue = heuristic(state)

    # if the player has won, return the heuristic value
    if (abs(heuristic) == 100):
        return heuristicValue

    if maxPlayer:
        pass
