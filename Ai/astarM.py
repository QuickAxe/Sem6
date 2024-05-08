heuristic = {
    "S": 14,
    "D": 12,
    "F": 12,
    "A": 11,
    "L": 10,
    "I": 10,
    "J": 8,
    "H": 8,
    "M": 7,
    "B": 10,
    "C": 8,
    "K": 6,
    "N": 4,
    "P": 5,
    "O": 8,
    "R": 6,
    "E": 5,
    "T": 3,
    "Q": 1,
    "G": 0,
}

graph = {
    "S": [("D", 25)],
    "D": [("F", 24), ("A", 32), ("S", 25), ("I", 26)],
    "F": [("L", 27), ("D", 24)],
    "A": [("D", 32), ("B", 11), ("H", 36)],
    "L": [("F", 27), ("I", 21), ("O", 26), ("M", 32)],
    "B": [("A", 11), ("K", 42), ("C", 24)],
    "I": [("D", 26), ("L", 21), ("J", 22)],
    "M": [("L", 32), ("P", 23), ("J", 20)],
    "P": [("M", 23)],
    "J": [("H", 22), ("I", 22), ("M", 20)],
    "H": [("A", 36), ("J", 22), ("N", 44), ("K", 28)],
    "C": [("B", 24), ("E", 40)],
    "E": [("C", 40), ("K", 32)],
    "K": [("E", 32), ("B", 42), ("H", 28), ("N", 27), ("Q", 62)],
    "N": [("K", 27), ("H", 44), ("Q", 32), ("G", 42)],
    "O": [("L", 26), ("R", 27)],
    "R": [("O", 27), ("T", 52)],
    "T": [("R", 52), ("G", 32)],
    "G": [("T", 32), ("N", 42)],
    "Q": [("N", 32), ("K", 62)],
}

open = []
closed = []
start = ("S", None, 0 + heuristic["S"])
goal = "G"
open.append(start)


def calc_f(neighbour_vertex, neighbour_vertex_dist, parent_state):
    return (
        parent_state[2]
        - heuristic[parent_state[0]]
        + dist
        + heuristic[neighbour_vertex]
    )


while len(open):
    curr_index = open.index(min(open, key=lambda t: t[2]))
    curr_state = open.pop(curr_index)
    closed.append(curr_state)
    if curr_state[0] == goal:
        print("Goal Reached!")
        break
    for neighbours in graph[curr_state[0]]:
        removal_index = -1
        # flag is set to False if better state exists in open
        flag_modify = True
        neighbour, dist = neighbours
        # Check if new neighbour is not in closed
        if not any(neighbour == visited[0] for visited in closed):
            new_state = (neighbour, curr_state[0], calc_f(
                neighbour, dist, curr_state))
            # If new neighbour is in open, it may require updation
            for index, current in enumerate(open):
                if neighbour == current[0] and new_state[2] < current[2]:
                    removal_index = index
                elif neighbour == current[0] and new_state[2] >= current[2]:
                    flag_modify = False

            if flag_modify:
                if removal_index >= 0:
                    open.pop(removal_index)
                open.append(new_state)

goal_state = closed[-1]
path_list = []
while not goal_state[1] is None:
    path_list.append(goal_state[0])
    for state in closed:
        goal_state = state if state[0] == goal_state[1] else goal_state
path_list.append("S")
path_list.reverse()
print("\nPath:")
for vertex in path_list[:-1]:
    print(f"{vertex} -> ", end="")
print(f"{path_list[-1]}")
print(f"Total Length:{closed[-1][2]}")
print("\nCLOSED list:")
print(*closed, sep="\n")
