m = int(input("Enter number of missionaries:"))
c = int(input("Enter number of cannibals:"))

START = (m, c, "L")
Visited = []
Visited.append(START)
Parent = {}
Parent[START] = None
GOAL = (0, 0, "R")


def DFSAdd(par_state, child_state):
    if child_state == GOAL:
        Parent[child_state] = par_state
        Rules(child_state)
    elif child_state not in Visited:
        m_, c_, _ = child_state
        # For balanced M & C on both sides
        # OR
        # No M on one side and all M on other side
        if m_ == c_ or m_ in [0, m]:
            Visited.append(child_state)
            Parent[child_state] = par_state
            Rules(child_state)


def Rules(curr_state):
    M, C, B = curr_state
    if curr_state == GOAL:
        global flag
        flag = 1

        path = []
        tup_ = curr_state
        while tup_ in Parent and Parent[tup_] is not None:
            path.append(tup_)
            tup_ = Parent[tup_]
        path.append(START)
        path.reverse()
        print(*path, sep="\n")
        print()
        return
    if B == "L":
        if M > 0 and C > 0:
            child_state = (M - 1, C - 1, "R")
            DFSAdd(curr_state, child_state)
        if M > 0:
            child_state = (M - 1, C, "R")
            DFSAdd(curr_state, child_state)
        if C > 0:
            child_state = (M, C - 1, "R")
            DFSAdd(curr_state, child_state)
        if C > c - 2:
            child_state = (M, C - 2, "R")
            DFSAdd(curr_state, child_state)
        if M > m - 2:
            child_state = (M - 2, C, "R")
            DFSAdd(curr_state, child_state)
    elif B == "R":
        if M < m and C < c:
            child_state = (M + 1, C + 1, "L")
            DFSAdd(curr_state, child_state)
        if M < m:
            child_state = (M + 1, C, "L")
            DFSAdd(curr_state, child_state)
        if C < c:
            child_state = (M, C + 1, "L")
            DFSAdd(curr_state, child_state)
        if C < c - 1:
            child_state = (M, C + 2, "L")
            DFSAdd(curr_state, child_state)
        if M < m - 1:
            child_state = (M + 2, C, "L")
            DFSAdd(curr_state, child_state)


flag = 0
Rules(START)

if not flag:
    print("ALAS! No solution...")
