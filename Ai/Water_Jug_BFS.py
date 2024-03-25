from queue import Queue

START = (0, 0, "Start")
Visited = []
Visited.append(START[:2])
Parent = {}
Parent[START] = None


def BFSPath(tuple, tup, q):
    Parent[tup] = tuple
    q.put(tup)
    Visited.append(tup[:2])


def Rules(tuple, GOAL_SET):

    q = Queue()
    q.put(tuple)

    while not q.empty():

        currtup = q.get()
        (jug1, jug2, type) = currtup

        if currtup[:2] in GOAL_SET:
            global flag
            flag = 1

            path = []
            tup_ = currtup

            while tup_ in Parent and Parent[tup_] is not None:
                path.append(tup_)
                tup_ = Parent[tup_]
            path.append(START)
            path.reverse()
            print(*path, sep=", ")
            print()

        else:

            if jug1 < m:
                tup = (m, jug2, "Filled jug1")

                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug2 < n:
                tup = (jug1, n, "Filled jug2")
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug1 > 0:
                tup = (0, jug2, "Emptied jug1")
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug2 > 0:
                tup = (jug1, 0, "Emptied jug2")
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug1 + jug2 < (m + n) and m - jug1 < jug2:
                tup = (
                    m,
                    jug2 - (m - jug1),
                    "Transferred jug2 to jug1 with some remaining",
                )
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug1 + jug2 < (m + n) and n - jug2 < jug1:
                tup = (
                    jug1 - (n - jug2),
                    n,
                    "Transferred jug1 to jug2 with some remaining",
                )
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug1 + jug2 < m:
                tup = (jug1 + jug2, 0, "Entirely transferred jug2 to jug1")
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)

            if jug1 + jug2 < n:
                tup = (0, jug1 + jug2, "Entirely transferred jug1 to jug2")
                if tup[:2] not in Visited:
                    BFSPath(currtup, tup, q)


m = int(input("Enter cap of jug1:"))
n = int(input("Enter cap of jug2:"))
g = int(input("Enter goal:"))
flag = 0
GOAL_SET = []

for i in range(n + 1):
    GOAL_SET.append((g, i))
for i in range(m + 1):
    GOAL_SET.append((i, g))
Rules(START, GOAL_SET)
if not flag:
    print("ALAS! No Solution!")
